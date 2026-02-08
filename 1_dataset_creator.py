import cv2
import os
import time

cascade_path = "haarcascade_frontalface_default.xml"
if not os.path.exists(cascade_path):
    print("Haarcascade file missing")
    exit()

student_id = input("Enter Student ID: ").strip()
student_name = input("Enter Student Name: ").strip()

dataset_dir = "dataset"
os.makedirs(dataset_dir, exist_ok=True)

student_folder = f"{dataset_dir}/{student_id}_{student_name}"
os.makedirs(student_folder, exist_ok=True)

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier(cascade_path)

poses = ["FRONT", "LEFT", "RIGHT"]
captured = 0

print("Follow instructions on screen.")

time.sleep(2)

while captured < 3:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    cv2.putText(frame, f"Show {poses[captured]} face",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    if len(faces) == 1:
        (x, y, w, h) = faces[0]
        face = gray[y:y+h, x:x+w]

        # Save image
        img_path = f"{student_folder}/{poses[captured].lower()}.jpg"
        cv2.imwrite(img_path, face)

        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        cv2.imshow("Register Student", frame)

        print(f"{poses[captured]} face captured")
        captured += 1
        time.sleep(2)  # give user time to turn head

    cv2.imshow("Register Student", frame)
    cv2.waitKey(1)

cam.release()
cv2.destroyAllWindows()

print("Dataset creation completed successfully (3 poses).")
