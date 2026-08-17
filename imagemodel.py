import numpy as np
import tensorflow as tf
from tensorflow import keras
import json

model = keras.models.load_model("/app/assets/gesture_mobilenet.keras")

img = keras.utils.load_img("/app/assets/thumbsUp.jpeg", target_size=(224, 224))
arr = keras.utils.img_to_array(img)
img_array = np.expand_dims(arr, 0)

output = model.predict(img_array, verbose=0)[0]

with open("/app/assets/gesture_classes.json") as f:
    classes = json.load(f)

predicted = classes["pretty"][int(np.argmax(output))]
print(f"Prediction: {predicted} ({np.max(output)*100:.1f}%)")