import requests
import numpy as np
from PIL import Image
import tensorflow as tf
import pickle

with open('scr/class_names.pickle', 'rb') as f:
    class_names = pickle.load(f)
model = tf.keras.models.load_model('scr/model')

def predict_class(img_url, model = model):
    img = Image.open(requests.get(img_url, stream=True).raw)
    tensor = tf.image.resize([np.array(img)], [256, 256])
    predict_data = model.predict(tensor)
    msg = 'Бобровость ' + str(round(predict_data[0][1] * 100, 1)) + '%'
    return class_names[np.argmax(predict_data)], msg