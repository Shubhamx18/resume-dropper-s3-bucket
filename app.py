import os
import uuid
import json
from flask import Flask, request, render_template, redirect, url_for
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# --- LOCAL MODE TOGGLE ---
# Set to True to run without AWS, printing data to the terminal instead.
# Set to False to use AWS S3.
LOCAL_MODE = False
# -------------------------

# Get AWS credentials and bucket name from environment variables
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")
bucket_name = os.getenv("S3_BUCKET")

# Validate that all required environment variables are set
if not LOCAL_MODE and not all([aws_access_key_id, aws_secret_access_key, aws_region, bucket_name]):
    raise ValueError("LOCAL_MODE is False but AWS environment variables are missing.")

# Initialize S3 client and test connection
s3 = None
if not LOCAL_MODE:
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region
        )
        # Test the connection and credentials by trying to list buckets
        s3.list_buckets()
        print("✅ AWS connection successful.")
    except Exception as e:
        print(f"❌ Could not connect to AWS. Please check your credentials and region in the .env file. Error: {e}")
        exit()

@app.route('/')
def index():
    """Render the main upload form."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    """Handle the file upload and metadata creation."""
    name = request.form.get('name')
    email = request.form.get('email')
    position = request.form.get('position')
    resume_file = request.files.get('resume')

    if not all([name, email, position, resume_file]):
        return "Missing form data", 400

    if resume_file and (resume_file.filename.endswith('.pdf') or resume_file.filename.endswith('.docx')):
        if LOCAL_MODE:
            print("\n--- LOCAL MODE: SIMULATING UPLOAD ---")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Position: {position}")
            print(f"Filename: {resume_file.filename}")
            print("-------------------------------------\n")
            return redirect(url_for('success', name=name))

        # Create a unique filename to avoid overwrites
        unique_filename = f"{uuid.uuid4()}_{resume_file.filename}"
        resume_file_key = f"resumes/{unique_filename}"

        try:
            # Upload resume to S3
            s3.upload_fileobj(resume_file, bucket_name, resume_file_key)

            # Create and upload metadata as a JSON file
            metadata = {
                "name": name,
                "email": email,
                "position": position,
                "resume_file_key": resume_file_key,
                "original_filename": resume_file.filename
            }
            metadata_key = f"metadata/{unique_filename}.json"
            s3.put_object(
                Bucket=bucket_name,
                Key=metadata_key,
                Body=json.dumps(metadata, indent=2)
            )

            return redirect(url_for('success', name=name))

        except Exception as e:
            print(f"Error uploading to S3: {e}")
            return "An error occurred during upload.", 500

    return "Invalid file type. Only .pdf and .docx are allowed.", 400

@app.route('/success')
def success():
    """Show a success message after upload."""
    name = request.args.get('name', 'there')
    return render_template('success.html', name=name)

@app.route('/admin')
def admin_view():
    """A simple admin view to list uploaded resumes."""
    if LOCAL_MODE:
        # In local mode, we can't list files from S3, so show a placeholder.
        return render_template('admin.html', submissions=[], local_mode=True)

    try:
        # List metadata files from S3
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix='metadata/')
        
        submissions = []
        if 'Contents' in response:
            for obj in response['Contents']:
                # Get each metadata file content
                meta_obj = s3.get_object(Bucket=bucket_name, Key=obj['Key'])
                meta_content = json.loads(meta_obj['Body'].read().decode('utf-8'))
                
                # Generate a presigned URL for the resume for temporary access
                resume_url = s3.generate_presigned_url(
                    'get_object',
                    Params={'Bucket': bucket_name, 'Key': meta_content['resume_file_key']},
                    ExpiresIn=3600  # URL expires in 1 hour
                )
                meta_content['download_url'] = resume_url
                submissions.append(meta_content)

        return render_template('admin.html', submissions=submissions, local_mode=False)

    except Exception as e:
        print(f"Error loading admin page: {e}")
        return "Could not load admin dashboard.", 500

if __name__ == '__main__':
    app.run(debug=True, port=5050) 