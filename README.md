
# 🎓 Online Examination System with AI-Powered Proctoring

This project is an advanced Online Examination System built with Django, React, and integrated AI proctoring using YOLOv8. It ensures fair, secure remote exams by detecting cheating behaviors such as multiple faces, unauthorized objects, tab switching, or exiting fullscreen.

---

## 🚀 Features

- 🔐 JWT-based authentication for students, teachers, and admins
- 📝 Exam creation with MCQs and subjective questions
- 🧠 Auto-grading for MCQs
- 📸 Proctoring using YOLOv8 (face & object detection)
- 🔎 Fullscreen enforcement and tab-switching detection
- ❌ Auto-disqualification on repeated violations
- 📊 Result management and dashboard for users

---

## ⚙️ Installation & Setup Guide

### 🔧 Prerequisites

- Python 3.10+
- Node.js 16+ & npm
- MongoDB Atlas account (or local MongoDB)
- Git

---

### 🐍 Backend Setup (Django + MongoDB)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name/backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run server**
   ```bash
   python manage.py runserver
   ```

---

### 🌐 Frontend Setup (React)

1. **Navigate to frontend**
   ```bash
   cd ../frontend
   ```

2. **Install packages**
   ```bash
   npm install
   ```

3. **Run frontend**
   ```bash
   npm start
   ```

---

## 🧠 Proctoring Using YOLOv8

- Captures webcam image every 5 seconds
- Image is decoded via OpenCV and passed to YOLOv8 for:
  - 🔍 Face detection (no face or multiple faces)
  - 📱 Object detection (phones, books, laptops)
- If a student violates rules 3 times, they are auto-disqualified

---

## 📦 Tech Stack

- **Frontend**: React.js
- **Backend**: Django REST Framework
- **Database**: MongoDB Atlas
- **Proctoring**: OpenCV + YOLOv8
- **YOLO Model Used**: `yolov8n.pt` (Nano)

---

## 📁 Project Structure

```
📁 backend/
  └── api/
      ├── views.py
      ├── models.py
      ├── urls.py
      └── yolo_demo.py
📁 frontend/
  └── src/
      ├── pages/
      ├── components/
      └── context/
```

---

## 📌 License

MIT License
