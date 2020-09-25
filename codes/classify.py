from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import http.client, urllib.request, urllib.parse, urllib.error, base64, os, io, json, requests, uuid

prediction_key = os.environ['PREDICTION_KEY']
project_id = os.environ['PROJECT_ID']
endpoint = os.environ['ENDPOINT']

def get_translation(img_input):
    base_url = endpoint
    path = "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/"+project_id+"/classify/iterations/Iteration1/sample1"
    #params = '&to=' + language_output
    constructed_url = base_url + path 

    headers = {
        'Content-Type': 'application/octet-stream',
        'Prediction-key': prediction_key,
    }

    # You can pass more than one object in body.

    response = requests.post(constructed_url, headers=headers, bytes=img_input)
    print (response.json())

#get_translation("https://i.ibb.co/gz0TFsC/P-test.jpg")