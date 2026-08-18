import cv2
import json
import numpy as np
import time
from tensorflow import keras

model = keras.models.load_model("/app/assets/gesture_mobilenet.keras")

with open("/app/assets/gesture_classes.json") as f:
    classes = json.load(f)

cap = cv2.VideoCapture(0)
ret, prev_frame = cap.read()
if not ret:
    raise RuntimeError("Could not read from webcam.")

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
#just to make sure the model is loaded and ready
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(prev_gray, gray)

    if diff.mean() > 25:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resized = cv2.resize(rgb_frame, (224, 224))
        img_array = np.expand_dims(resized.astype(np.float32), axis=0)
        output = model.predict(img_array, verbose=0)[0]
        predicted = classes["pretty"][int(np.argmax(output))]
        confidence = np.max(output) * 100
        if confidence > 80: 
             print(f"Prediction: {predicted} ({confidence:.1f}%)", flush=True)

    prev_gray = gray
    time.sleep(0.2)




cap.release()