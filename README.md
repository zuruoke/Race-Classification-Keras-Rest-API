# Race-Classification-Keras-Rest-API
A Simple Keras Rest API for Race Classification  


# Getting started

I assume you already have numpy, pillow, Keras and a supported backend (tensorflow in this case) installed on your system. From there you need to install Flask, urllib, flask_restful and requests:
                
                
                                    $ pip install flask gevent flask_restful requests
                                    

Next, clone the repo:
                            
                            $ git clone https://github.com/zuruoke/Race-Classification-Keras-Rest-API.git
                            

Next, navigate into the main directory:
                              
                              $ cd Race-Classification-Keras-Rest-API
                          


# Starting the Keras server

Below is our query image (kim.jpg) we wish to classify as either a  Caucasian, Mongoloid or a Negroid:

![kim](https://user-images.githubusercontent.com/51057490/87179658-fce6de80-c2d6-11ea-8355-7c12fb436745.jpg)

The Flask + Keras server can be started by running:

                              $ python run_keras_server.py 
                              Using TensorFlow backend.
                              * Loading Zuruoke model and Flask starting server...please wait until server has fully started
                              ...
                              * Running on http://127.0.0.1:1000
                              
You can now access the REST API via http://localhost:1000. 

We will use this url attached with an endpoint to send a POST request to the server. In this case:

                             KERAS_REST_API_URL = "http://localhost:1000/predict"
                             
                             
# Consuming the Keras REST API

We have to send a POST request to the server running to consume the API.

To consume the Keras REST API:

- First ensure run_keras_server.py (i.e., the Flask web server) is currently running

- Then open another terminal in the same environment and navigate to the main directory

- Then run post_request.py

                            $ python post_request.py
                            
- Then you will be asked to enter the image path of the query image you want to classify
                                
                             $ python post_request.py
                             Enter the image path:
                             kim.jpg
                             
 
 - And then when you have provided the query image path, it will output the predictions along with the probabilities or confidence level
 
                             $ python post_request.py
                             Enter the image path:
                             kim.jpg
                             1. Caucasian: 0.7900
                             2. Mongoloid: 99.2011
                             3. Negroid: 0.0089

                            

