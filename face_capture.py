"""This module provides functions for capturing and saving face images of students using a webcam and OpenCV.
"""

import cv2
from config import FACE_CASCADE, DATA_PATH

def capture_face(name, count=20):
    cap = cv2.VideoCapture(0)
    idx = 0
    print(f"Capturing face samples for {name}...")
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            idx += 1
            face_img = gray[y:y+h, x:x+w]
            face_img = cv2.resize(face_img, (100, 100))
            cv2.imwrite(f"{DATA_PATH}/{name}_{idx}.jpg", face_img)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("Capture Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or idx >= count:
            break
    cap.release()
    cv2.destroyAllWindows()
    print(f"{idx} samples saved for {name}.")
