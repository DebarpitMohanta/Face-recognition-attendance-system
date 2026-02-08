import cv2
import numpy as np
import pandas as pd
import dlib
import os
from imutils import face_utils
from scipy.spatial import distance as dist
from datetime import datetime
import time

# ---------- CHECKS ----------
if not os.path.exists("trainer/trainer.yml"):
    print("Model not trained yet")
    exit()

# ---------- BLINK FUNCTION ----------
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

EYE_THRESH = 0.23
EYE_FRAMES = 3
blink_count = 0
attendance_marked = False

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cam = cv2.VideoCapture(0)

if not os.path.exists("attendance.csv"):
    pd.DataFrame(columns=["ID","Date","Time"]).to_csv("attendance.csv", index=False)

attendance = pd.read_csv("attendance.csv")

print("Attendance started. Blink to mark attendance.")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 1:
        cv2.putText(frame, "Only ONE person allowed", (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        cv2.imshow("Attendance", frame)
        continue

    for (x,y,w,h) in faces:
        roi = gray[y:y+h, x:x+w]
        id, _ = recognizer.predict(roi)

        shape = predictor(gray, dlib.rectangle(x,y,x+w,y+h))
        shape = face_utils.shape_to_np(shape)
        leftEye = shape[36:42]
        rightEye = shape[42:48]

        ear = (eye_aspect_ratio(leftEye)+eye_aspect_ratio(rightEye))/2

        if ear < EYE_THRESH:
            blink_count += 1
        else:
            if blink_count >= EYE_FRAMES and not attendance_marked:
                now = datetime.now()
                attendance.loc[len(attendance)] = [id, now.date(), now.strftime("%H:%M:%S")]
                attendance.to_csv("attendance.csv", index=False)
                attendance_marked = True
                print("Attendance marked. Exiting...")
                time.sleep(2)
                cam.release()
                cv2.destroyAllWindows()
                exit()
            blink_count = 0

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("Attendance (Blink once)", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
print("Attendance session ended.")