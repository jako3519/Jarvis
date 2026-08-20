import cv2
import json
import numpy as np
import time
from collections import defaultdict
from tensorflow import keras
import paho.mqtt.client as mqtt
import time

while True:
    try:
        mqtt_client = mqtt.Client()
        mqtt_client.connect("mosquitto", 1883)
        print("Forbundet til Mosquitto!", flush=True)
        break
    except Exception as e:
        print(f"Venter på Mosquitto... {e}", flush=True)
        time.sleep(2)

model = keras.models.load_model("/app/assets/gesture_mobilenet.keras")

with open("/app/assets/gesture_classes.json") as f:
    classes = json.load(f)

cap = cv2.VideoCapture(0)
ret, prev_frame = cap.read()
if not ret:
    raise RuntimeError("Could not read from webcam.")

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

counts = defaultdict(int)
last_prediction = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(prev_gray, gray)

    if diff.mean() > 5:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resized = cv2.resize(rgb_frame, (224, 224))
        img_array = np.expand_dims(resized, axis=0)
        output = model.predict(img_array, verbose=0)[0]
        predicted = classes["pretty"][int(np.argmax(output))]
        confidence = np.max(output) * 100

        if confidence > 90:
            if predicted != last_prediction:
                counts.clear()
                last_prediction = predicted
            
            counts[predicted] += 1
            print(f"{predicted}: {counts[predicted]}/5 ({confidence:.1f}%)", flush=True)

            if counts[predicted] >= 5:
                mqtt_client.publish("jarvis/gesture", predicted)
                print(f"SENT: {predicted}", flush=True)
                counts.clear()
                last_prediction = None

    prev_gray = gray
    time.sleep(0.1)

cap.release()