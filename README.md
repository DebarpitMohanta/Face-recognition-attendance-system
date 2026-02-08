# Face Recognition Based Automated Attendance System

A secure, real-time automated attendance system built using Python, OpenCV, and dlib that detects and recognizes faces, verifies liveness using eye-blink detection, and records attendance automatically.

---

## 🚀 Features

- 🎯 Face detection using OpenCV Haarcascade
- 🧠 Face recognition using LBPH algorithm
- 👁 Eye-blink liveness detection (prevents photo/video proxy)
- 👤 Single-user validation (blocks multiple faces)
- 📸 Controlled dataset capture (Front / Left / Right)
- 🖥 Simple Tkinter GUI interface
- 🗂 Automatic attendance logging in CSV format
- ⚡ Real-time processing using webcam

---

## 🛠 Tech Stack

- Python  
- OpenCV (opencv-contrib-python)  
- dlib  
- NumPy  
- Pandas  
- Tkinter
## Required Model Files

Download the following file manually and place it in the project root folder:

shape_predictor_68_face_landmarks.dat  
Download link: http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

## 📸 Screenshots

### GUI Interface
![GUI](screenshots/gui.png)

### Attendance Log
![CSV](screenshots/csv.png)

### System Running (Terminal Output)
![Terminal](screenshots/Terminal%20running.png)

## ⚠ Note:
The shape_predictor_68_face_landmarks.dat file is not included due to size constraints.
Please download it manually from the official dlib website.


## 📁 Project Structure
Face_Attendance_System/
│
├── dataset/ # Stored face images
├── trainer/ # Trained model
├── attendance.csv # Attendance records
│
├── 1_dataset_creator.py # Capture face dataset
├── 2_trainer.py # Train LBPH model
├── 3_attendance.py # Face recognition + blink detection
├── main_gui.py # GUI controller
│
├── haarcascade_frontalface_default.xml
├── shape_predictor_68_face_landmarks.dat
