# Technologies used

1) Django
2) RestFramework
3) JWT
4) Cloudinary

# 📚 Django Library Management System API

A simple, structured guide to setting up and running the Django-based Library Management System API.

---

## ⚙️ Setup Instructions

### 🐍 Create & Activate Virtual Environment

```bash
python3 -m venv venv           # Create a virtual environment
source venv/bin/activate       # Activate the environment
```

## 🚀 Django Project Setup Guide

This guide provides essential commands and best practices for setting up and managing your Django project.

---

## 🛠 Project Initialization

### 🧱 Start a New Django Project

```bash
django-admin startproject project
```

>🔸 This command creates a project with a subfolder named project. To avoid the extra directory:
```bash
django-admin startproject project .
```

### creating the api folder inside project
```base
python manage.py startapp api 
```
### Make sure to update the settings in core/settings.py
```base
INSTALLED_APPS = [
    # External packages
    "rest_framework",
    "rest_framework_simplejwt",
    # Internal apps
    "api",
    # Cloudinary apps
    "cloudinary",
    "cloudinary_storage",
]
```
### 🔧 Always update the settings.py file when adding new apps or packages.

### 📅 Install Dependencies (for Cloned Repositories)
```bash
pip install -r requirements.txt
```

### 📂 Update/Create requirements.txt
```bash
pip freeze > requirements.txt
```

## Database operations

### ❌ Reset the Database (Optional)

```bash
rm db.sqlite3  # or drop the database if using PostgreSQL/MySQL
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
```
### 🛠️ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 🧪 Run the Development Server
```bash
python manage.py runserver
```
🌐 Visit: http://127.0.0.1:8000


