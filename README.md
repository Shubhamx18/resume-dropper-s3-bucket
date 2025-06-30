
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
