from face_capture import capture_face
from face_recognition import recognize_face
from attendance_manager import mark_attendance, init_excel
import os
from config import EXCEL_FILE

def view_attendance(pending_name=None):
    if pending_name:
        mark_attendance(pending_name)
    init_excel()
    try:
        os.startfile(EXCEL_FILE) # Windows only
    except Exception as e:
        print(f"Could not open Excel file: {e}")

def main():
    pending_name = None
    while True:
        print("\nMENU")
        print("1. Capture Student Face")
        print("2. Start Attendance")
        print("3. View Attendance Sheet")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            student_name = input("Enter student name: ")
            capture_face(student_name)
        elif choice == '2':
            pending_name = recognize_face()
        elif choice == '3':
            view_attendance(pending_name)
            pending_name = None
        elif choice == '4':
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
