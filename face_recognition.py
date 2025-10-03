import cv2
import numpy as np
import os
import time
from config import DATA_PATH, FACE_CASCADE

def recognize_face():
    samples = {}
    for file in os.listdir(DATA_PATH):
        name = file.split('_')[0] #Ensure name is string
        print("DEBUG file:", file, type(file))  # Add this line
        if isinstance(file, list):
            file = str(file)  # Ensure 'file' is a string
        #name = file.split('_')
        img = cv2.imread(os.path.join(DATA_PATH, file), cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"Warning: Unable to load image {file}")
            continue
        samples.setdefault(name, []).append(img)
    cap = cv2.VideoCapture(0)
    print("Recognition started. Please look at the camera.")
    start_time = time.time()
    while True:
        if time.time() - start_time > 30:
            print("No known person detected. Camera shutting down.")
            cap.release()
            cv2.destroyAllWindows()
            return None
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = FACE_CASCADE.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face_img = cv2.resize(gray[y:y+h, x:x+w], (100, 100))
            best_match = None
            lowest_score = float("inf")
            for name, imgs in samples.items():
                for sample in imgs:
                    score = np.sum((face_img - sample) ** 2)
                    if score < lowest_score:
                        lowest_score = score
                        best_match = name
            label = best_match if lowest_score < 1e6 else "Unknown"
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (0, 255, 0) if label != "Unknown" else (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h),
                          (0, 255, 0) if label != "Unknown" else (0, 0, 255), 2)
            cv2.imshow("Attendance", frame)
            cv2.waitKey(1500)
            cap.release()
            cv2.destroyAllWindows()
            return label if label != "Unknown" else None
