from flask import Flask, render_template, request, jsonify, url_for
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from PIL import Image
import http.client, urllib.request, urllib.parse, urllib.error, base64, os, io, classify


def best_emotion(emotion):
  emotions = {}
  emotions['with-mask'] = emotion.with-mask
  emotions['without-mask'] = emotion.without-mask
  return max(zip(emotions.values(), emotions.keys()))[1]


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/classify', methods=['POST'])
def classify():
    body = request.get_json()
    print(body['image_base64'])
    image_bytes = base64.b64decode(body['image_base64'].split(',')[1])
    #image = io.BytesIO(image_bytes)
    #image = Image.open(io.BytesIO(image_bytes))
    #image.save(savepath)


    response = classify.get_translation(image_bytes)
    return jsonify(response)
