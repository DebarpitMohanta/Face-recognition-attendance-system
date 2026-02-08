# Face Recognition Based Automated Attendance System

A secure, real-time automated attendance system built using Python, OpenCV, and dlib.  
The system detects and recognizes faces, verifies liveness using eye-blink detection, and automatically records attendance in CSV format.

---

## 🚀 Features

- 🎯 Face detection using OpenCV Haarcascade  
- 🧠 Face recognition using LBPH algorithm  
- 👁 Eye-blink liveness detection (prevents photo/video proxy)  
- 👤 Single-user validation (blocks multiple faces)  
- 📸 Automatic dataset capture (Front / Left / Right angles)  
- 🖥 Simple Tkinter GUI interface  
- 🗂 Automatic attendance logging in CSV format  
- ⚡ Real-time webcam processing  

---

## 🛠 Tech Stack

- Python  
- OpenCV (opencv-contrib-python)  
- dlib  
- NumPy  
- Pandas  
- Tkinter  

---

## 📥 Required Model File (Manual Download)

Due to large file size, the dlib landmark model is not included in the repository.

Download and place in the project root folder:

Download link:
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

Extract after downloading.

---

## ⚙️ Installation

Install dependencies:


---

## ▶️ How to Run

Start the system:


### Workflow:

1. Register Student → captures face images  
2. Train Model → creates trained recognizer  
3. Take Attendance → detects + verifies + logs  

---

## 📸 Screenshots

### GUI Interface
![GUI](screenshotsgui.png)

### Attendance Log
![CSV](screenshotscsv.png)

### System Running (Terminal Output)
![Terminal](screenshotsterminal.png)

---

## 📁 Project Structure
Face-recognition-attendance-system/
│
├── dataset/                         # Auto-created folder (stores captured face images)
│   └── [student_id]_[name]/
│       ├── img1.jpg
│       ├── img2.jpg
│       └── img3.jpg
│
├── trainer/                         # Auto-created after training
│   └── trainer.yml                  # Trained LBPH model file
│
├── attendance.csv                   # Auto-generated attendance records
│
├── 1_dataset_creator.py             # Capture student face dataset
├── 2_trainer.py                     # Train LBPH face recognition model
├── 3_attendance.py                  # Face recognition + blink detection
├── main_gui.py                      # GUI controller (main entry point)
│
├── haarcascade_frontalface_default.xml   # Face detection model
├── shape_predictor_68_face_landmarks.dat # Dlib landmark model (manual download)
├── requirements.txt                 # Python dependencies
│
├── screenshotsgui.png               # GUI preview image
├── screenshotscsv.png               # Attendance log preview
├── screenshotsterminal.png          # System running preview
│
└── README.md

## 🎯 Project Type

Final Year Major Project  
Domain: Computer Vision / AI / Automation


---

## 🔐 Security Feature

This system uses eye-blink based liveness detection to ensure attendance is marked only when a real person is present, preventing spoofing using photos or videos.

---

## 📊 Output

Attendance is automatically saved in:


Includes:
- Student ID  
- Date  
- Time  

---

## 🎯 Project Type

Final Year Major Project  
Domain: Computer Vision / AI / Automation
## ⚠ Note:
The shape_predictor_68_face_landmarks.dat file is not included due to size constraints.
Please download it manually from the official dlib website.

