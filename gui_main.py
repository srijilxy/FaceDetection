import tkinter as tk
from tkinter import messagebox
from face_capture import capture_face
from face_recognition import recognize_face
from attendance_manager import mark_attendance, init_excel
import os
from config import EXCEL_FILE

# Create main window
root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("400x300")

# Example label
label = tk.Label(root, text="Attendance System", font=("Arial", 16))
label.pack(pady=20)  #-  means there's 20 pixels of vertical space above and below the label.



def capture_face_gui():
    # To be linked to your capture_face function
    def on_submit():
        name = name_entry.get()
        if name:
            capture_face(name)
        popup.destroy()
    popup = tk.Toplevel(root)
    popup.title("Capture Face")
    tk.Label(popup, text="Enter Student Name: ").pack(pady=10)
    name_entry = tk.Entry(popup)
    name_entry.pack(pady=5)
    tk.Button(popup, text="Start Capture", command=on_submit).pack(pady=10)
    pass


def start_attendance_gui():
    # To be linked to your recognize_face function
    recognized_name = recognize_face()  # This launches the camera for recognition
    if recognized_name:
        mark_attendance(recognized_name)
        messagebox.showinfo("Attendance", f"{recognized_name} marked as present!")
    else:
        messagebox.showwarning("Attendance", "No recognized face detected.")
    pass


def view_attendance_gui():
    # To be linked to your attendance viewing logic
    init_excel()
    try:
        os.startfile(EXCEL_FILE)
    except Exception as e:
        messagebox.showerror("Error", f"Could not open Excel file: {e}")
    pass


capture_btn = tk.Button(root, text="Capture Student Face", width=30, command=capture_face_gui)
capture_btn.pack(pady=10)

start_btn = tk.Button(root, text="Start Attendance", width=30, command=start_attendance_gui)
start_btn.pack(pady=10)

view_btn = tk.Button(root, text="View Attendance Sheet", width=30, command=view_attendance_gui)
view_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", width=30, command=root.quit)
exit_btn.pack(pady=10)



# Start main event loop
root.mainloop()
    # else:
    #     messagebox.showinfo("Info", f"{name} has already marked attendance today.")