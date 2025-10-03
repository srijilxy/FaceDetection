import cv2
import os

DATA_PATH = "faces_db"
EXCEL_FILE = "Attendance.xlsx"
FACE_CASCADE = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
os.makedirs(DATA_PATH, exist_ok=True)
