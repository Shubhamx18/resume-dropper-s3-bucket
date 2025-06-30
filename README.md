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