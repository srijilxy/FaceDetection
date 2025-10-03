# import cv2
# import numpy as np
# import os
# import datetime
# from openpyxl import Workbook, load_workbook
# import time

# # Paths and classifier
# data_path = "faces_db"
# excel_file = "Attendance.xlsx"
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# os.makedirs(data_path, exist_ok=True)

# def init_excel():
#     if not os.path.exists(excel_file):
#         wb = Workbook()
#         ws = wb.active
#         ws.title = "Attendance"
#         ws.append(["Name", "Attendance", "Date", "Time"])
#         wb.save(excel_file)

# def mark_attendance(name):
#     init_excel()
#     now = datetime.datetime.now()
#     date_str = now.strftime("%d-%m-%y")
#     time_str = now.strftime("%H:%M:%S")
#     wb = load_workbook(excel_file)
#     ws = wb["Attendance"]
#     names_today = [row[0].value for row in ws.iter_rows(min_row=2) if row[2] == date_str]
#     if name not in names_today:
#         ws.append([name, "Present", date_str, time_str])
#         wb.save(excel_file)

# def capture_face(name, count=20):
#     cap = cv2.VideoCapture(0)
#     idx = 0
#     print(f"Capturing face samples for {name}...")
#     while True:
#         ret, frame = cap.read()
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#         for (x, y, w, h) in faces:
#             idx += 1
#             face_img = gray[y:y+h, x:x+w]
#             face_img = cv2.resize(face_img, (100, 100))
#             cv2.imwrite(f"{data_path}/{name}_{idx}.jpg", face_img)
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         cv2.imshow("Capture Face", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q') or idx >= count:
#             break
#     cap.release()
#     cv2.destroyAllWindows()
#     print(f"{idx} samples saved for {name}.")

# def recognize_face():
#     samples = {}
#     for file in os.listdir(data_path):
#         name = file.split('_')[0]
#         img = cv2.imread(os.path.join(data_path, file), cv2.IMREAD_GRAYSCALE)
#         samples.setdefault(name, []).append(img)

#     cap = cv2.VideoCapture(0)
#     print("Recognition started. Please look at the camera.")
#     start_time = time.time()

#     while True:
#         if time.time() - start_time > 30:
#             print("No known person detected. Camera shutting down.")
#             cap.release()
#             cv2.destroyAllWindows()
#             return None

#         ret, frame = cap.read()
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#         for (x, y, w, h) in faces:
#             face_img = cv2.resize(gray[y:y+h, x:x+w], (100, 100))
#             best_match = None
#             lowest_score = float("inf")
#             for name, imgs in samples.items():
#                 for sample in imgs:
#                     score = np.sum((face_img - sample) ** 2)
#                     if score < lowest_score:
#                         lowest_score = score
#                         best_match = name

#             label = best_match if lowest_score < 1e6 else "Unknown"
#             cv2.putText(frame, label, (x, y-10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.8,
#                         (0, 255, 0) if label != "Unknown" else (0, 0, 255), 2)
#             cv2.rectangle(frame, (x, y), (x+w, y+h),
#                           (0, 255, 0) if label != "Unknown" else (0, 0, 255), 2)
#             cv2.imshow("Attendance", frame)
#             cv2.waitKey(1500)
#             cap.release()
#             cv2.destroyAllWindows()
#             return label if label != "Unknown" else None

#         cv2.imshow("Attendance Camera", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     return None

# def view_attendance(pending_name=None):
#     if pending_name:
#         mark_attendance(pending_name)
#     init_excel()
#     try:
#         os.startfile(excel_file)  # Windows only
#     except Exception as e:
#         print(f"Could not open Excel file: {e}")

# # Main menu
# pending_name = None

# while True:
#     print("\nMENU")
#     print("1. Capture Student Face")
#     print("2. Start Attendance")
#     print("3. View Attendance Sheet")
#     print("4. Exit")
#     choice = input("Choose an option: ")
#     if choice == '1':
#         student_name = input("Enter student name: ")
#         capture_face(student_name)
#     elif choice == '2':
#         pending_name = recognize_face()
#     elif choice == '3':
#         view_attendance(pending_name)
#         pending_name = None
#     elif choice == '4':
#         print("Program ended.")
#         break
#     else:
#         print("Invalid choice. Please try again.")