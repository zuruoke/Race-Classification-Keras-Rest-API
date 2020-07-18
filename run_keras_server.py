import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D, BatchNormalization, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import Model
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Concatenate, Input, ZeroPadding2D
from tensorflow.keras.losses import mean_squared_error, mean_absolute_error
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import time
import io
import os
import numpy as np
from tensorflow.keras.layers import Input, Dense, Reshape, Flatten, Dropout
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.layers import UpSampling2D, Conv2D, Conv2DTranspose
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam
import sys
import urllib
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import flask
from tensorflow.keras.models import model_from_json
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
#from flask_ngrok import run_with_ngrok

app = flask.Flask(__name__)
#run_with_ngrok(app)
model = None


def load_model():
    # load the pre-trained Keras model (here we are using a model
    # pre-trained on ImageNet and provided by Keras, but you can
    # substitute in your own networks just as easily)
    urllib.request.urlretrieve("https://github.com/zuruoke/Race-Classification-Keras-Rest-API/releases/download/v0.1-alpha/race_model.json", "arch.json")
    urllib.request.urlretrieve("https://github.com/zuruoke/Race-Classification-Keras-Rest-API/releases/download/v0.1-alpha/race.h5", "RACE.h5")

    model_architecture = 'arch.json'
    model_weights = "RACE.h5"
    global model

    model = model_from_json(open(model_architecture).read())	
    model.load_weights(model_weights)
	


def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)

    # return the processed image
    return image



@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
   
    data = {"success": False}
    result_label = ["Caucasian","Mongoloid", "Negroid"]
    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image in PIL format
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))

            # preprocess the image and prepare it for classification
            image = prepare_image(image, target=(128, 128))

            # classify the input image and then initialize the list
            # of predictions to return to the client
            result_score = []
            pred = model.predict(image)

            for grn in pred:
            	for sc in grn:
            		result_score.append(100 * sc)

			
            data["predictions"] = []

            for label, score in zip(result_label, result_score):
            	r = {"label":label, "probability": float(score)}
            	data["predictions"].append(r)
			
			
            data["success"] = True	

    return flask.jsonify(data)        
	
  	
            



if __name__ == "__main__":
    print(("* Loading Zuruoke model and Flask starting server..."
        "please wait until server has fully started"))
    load_model()
    app.run(port=1000, debug=True)            
