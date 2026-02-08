import tkinter as tk
import os
import sys

PYTHON = sys.executable

def run_dataset():
    os.system(f'"{PYTHON}" 1_dataset_creator.py')

def run_trainer():
    os.system(f'"{PYTHON}" 2_trainer.py')

def run_attendance():
    os.system(f'"{PYTHON}" 3_attendance.py')

root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("420x360")
root.resizable(False, False)

tk.Label(
    root,
    text="Face Recognition Based\nAutomated Attendance System",
    font=("Arial", 14, "bold"),
    pady=20
).pack()

tk.Button(root, text="Register Student", width=30, height=2, command=run_dataset).pack(pady=8)
tk.Button(root, text="Train Model", width=30, height=2, command=run_trainer).pack(pady=8)
tk.Button(root, text="Take Attendance", width=30, height=2, command=run_attendance).pack(pady=8)
tk.Button(root, text="Exit", width=30, height=2, command=root.quit).pack(pady=15)

root.mainloop()
