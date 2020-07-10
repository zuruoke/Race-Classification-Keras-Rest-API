import requests
from flask_restful import reqparse
# initialize the Keras REST API endpoint URL along with the input
# image path
IMAGE_PATH = input("Enter the image path:\n")

KERAS_REST_API_URL = "http://localhost:1000/predict"
	#IMAGE_PATH = "harrt.jpg"

	#parser = reqparse.RequestParser()
	#parser.add_argument('query')

	#args = parser.parse_args()
	#user_query = args['query']
	# load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

# submit the request
r = requests.post(KERAS_REST_API_URL, files=payload).json()

if r["success"]:

	for (i, Result) in enumerate(r["predictions"]):
		print("{}. {}: {:.4f}".format(i + 1, Result["label"], Result["probability"]))


else:
	print("Request Failed")
