<<<<<<< HEAD
# 🚀 RecruitDrop – Resume Submission Portal

A beautiful, modern web app for collecting job applications and resumes. Built with Flask, styled with glassmorphism, and supports both local testing and AWS S3 cloud storage.

---

## 🌟 Features
- Responsive, modern UI (glassmorphism, gradients, floating labels)
- User form for name, email, position, and resume upload (.pdf/.docx)
- Admin dashboard to view/download all submissions
- **Local mode**: test without AWS
- **Cloud mode**: store resumes and metadata in S3

---

## 🗂️ Project Structure
```
S3_/
├── app.py
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── success.html
│   └── admin.html
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repo & Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Local Mode (No AWS Required)
- In `app.py`, set:
  ```python
  LOCAL_MODE = True
  ```
- Run the app:
  ```bash
  python app.py
  ```
- Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.
- Submissions print to the terminal. Admin dashboard shows a local mode warning.

### 3. Cloud Mode (AWS S3 Integration)
- In `app.py`, set:
  ```python
  LOCAL_MODE = False
  ```
- Create a `.env` file in your project root:
  ```ini
  AWS_ACCESS_KEY_ID=your-access-key
  AWS_SECRET_ACCESS_KEY=your-secret-key
  AWS_REGION=your-region
  S3_BUCKET=your-bucket-name
  ```
- Make sure your IAM user has full S3 permissions and the bucket exists.
- Run the app:
  ```bash
  python app.py
  ```
- You should see `✅ AWS connection successful.`
- Submissions are stored in S3 and visible in the admin dashboard.

---

## 📝 .env Example
```
AWS_ACCESS_KEY_ID=AKIAxxxxxxxxxxxxxxxx
AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
AWS_REGION=us-east-1
S3_BUCKET=resume-dropper-bucket
```

---

## 💡 Customization
- Edit `static/style.css` for colors, spacing, or branding.
- Add more fields to the form in `templates/index.html` as needed.
- Extend admin features as you wish!

---

## 🛡️ License
MIT License. Free for personal and commercial use.

---

## 👨‍💻 Author
Open source project. Contributions welcome! 
=======

# 🚀 S3 Static Website – Host HTML/CSS/JS via AWS S3

This project demonstrates how to host a fully static website (HTML, CSS, JavaScript) using **Amazon S3**. It's ideal for portfolios, landing pages, project demos, or any frontend project that doesn't require a backend.

---

## 🌩️ 1. AWS Setup Guide

### 🔐 IAM User Setup

1. Go to **AWS Console → IAM → Users → Add user**
2. Enter a username (e.g., `s3-static-user`)
3. Enable ✅ **Programmatic access**
4. Click **Next → Attach existing policies directly**
5. Select ✅ `AmazonS3FullAccess`
6. Complete creation and save your:
   - **Access Key ID**
   - **Secret Access Key**

---

### 🪣 Create an S3 Bucket

1. Go to **S3 → Create Bucket**
2. Bucket name: must be **globally unique** (e.g., `static-website-hosting-using-s3-bucket1`)
3. Choose **Region**: `us-east-1` (or your preferred region)
4. Uncheck ✅ **Block all public access**
5. Enable static website hosting:
   - **Index document**: `index.html`
   - **Error document** (optional): `error.html`
6. Click **Create Bucket**

---

### 📁 2. Project Folder Structure
my-static-site/
├── index.html
├── style.css
├── script.js
└── images/

### Upload Project Files
1)upload the project to your s3 bucket from your device so to proceed.....
2) Go into the permissions and 

Add Bucket Policy to Allow Public Access
Create a file bucket-policy.json:

json
Copy
Edit
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::static-website-hosting-using-s3-bucket1/*"
    }
  ]
}
apply it....
###
After this you can get a url of hosted website from where you can access it 

You Can Access my website >>
http://static-website-hosting-using-s3-bucket1.s3-website.ap-south-1.amazonaws.com
>>>>>>> adc633129dffcf67f2bea4262308e7b344b01b3e
