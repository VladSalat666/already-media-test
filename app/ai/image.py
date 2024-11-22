from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np
from PIL import Image

model = MobileNetV2(weights='imagenet')


def classify_image(image):
  sized_img = Image.open(image).resize((224, 224))

  img_np_array = np.array(sized_img)
  img_np_array = np.expand_dims(img_np_array, axis=0)
  img_np_array = preprocess_input(img_np_array)

  predictions = model.predict(img_np_array)
  decoded_predictions = decode_predictions(predictions, top=3)[0]

  return [(class_name, score) for (_, class_name, score) in decoded_predictions]
