# Attandence Project

## Overview
This project is an attendance management system that uses face recognition to automate the process of recording attendance. It includes a Python-based GUI, face capture and recognition modules, and a web interface built with Django for managing attendance records.

## Features
- Face recognition for attendance marking
- GUI for user interaction
- Attendance data stored in Excel and SQLite
- Django web application for attendance management
- Employee face database for recognition

## Folder Structure
- `attendance_manager.py` - Main logic for attendance management
- `Attendence.py` - Additional attendance logic
- `config.py` - Configuration settings
- `face_capture.py` - Captures face images for database
- `face_recognition.py` - Recognizes faces for attendance
- `gui_main.py` - Main GUI application
- `main.py` - Entry point for the project
- `tkinder_note.py` - Tkinter notes and helpers
- `Attendance.xlsx` - Excel file for attendance records
- `faces_db/` - Folder containing face images for recognition
- `attendance_web/` - Django web application
  - `attendance/` - Django app for attendance
  - `attendance_web/` - Django project settings
  - `db.sqlite3` - SQLite database for web app
  - `manage.py` - Django management script

## Setup Instructions

### 1. Install Required Python Packages
Activate your virtual environment (if using one), then run:
```powershell
pip install opencv-python numpy openpyxl django
```

### 2. Run the GUI Application
From the project root, execute:
```powershell
python Attandence/gui_main.py
```

### 3. Run the Django Web Application
Navigate to the Django project folder and start the server:
```powershell
cd Attandence/attendance_web
python manage.py runserver
```

### 4. Usage
- Use the GUI to capture faces and mark attendance.
- Access the web interface at `http://127.0.0.1:8000/` to view and manage attendance records.

## Usage
- Use the GUI to capture faces and mark attendance.
- Access the web interface to view and manage attendance records.

## Requirements
- Python 3.8+
- opencv-python
- numpy
- openpyxl
- django
- Tkinter (included with Python)

## License
This project is provided for educational purposes only. Commercial use is not permitted without explicit permission.
