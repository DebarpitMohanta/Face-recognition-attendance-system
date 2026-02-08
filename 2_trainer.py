import cv2
import numpy as np
import os
from PIL import Image

cascade_path = "haarcascade_frontalface_default.xml"
dataset_path = "dataset"

if not os.path.exists(dataset_path):
    print("Dataset folder not found!")
    exit()

recognizer = cv2.face.LBPHFaceRecognizer_create()
faces = []
ids = []

for folder in os.listdir(dataset_path):
    try:
        id = int(folder.split("_")[0])
    except:
        continue

    folder_path = os.path.join(dataset_path, folder)

    for image in os.listdir(folder_path):
        img_path = os.path.join(folder_path, image)
        img = Image.open(img_path).convert('L')
        img_np = np.array(img, 'uint8')
        faces.append(img_np)
        ids.append(id)

if len(faces) == 0:
    print("No face data found!")
    exit()

os.makedirs("trainer", exist_ok=True)
recognizer.train(faces, np.array(ids))
recognizer.save("trainer/trainer.yml")

print("Model Trained Successfully")
