import json
import os
from flask import Flask,jsonify,request
from flask_cors import CORS
from predictor import my_location_predictor

app = Flask(__name__)
CORS(app)
@app.route("/predict",methods=['GET'])
def return_price():
  minSize = request.args.get('minSize')
  maxSize = request.args.get('maxSize')
  minRent = request.args.get('minRent')
  maxRent = request.args.get('maxRent')
  price = my_location_predictor.predict(minSize, maxRent, year) 
  price_dict = {
                'model':'mlp',
                'price': price,
                }
  return jsonify(price_dict)

@app.route("/",methods=['GET'])
def default():
  return "<h1> Welcome to bitcoin price predictor <h1>"

if __name__ == "__main__":
    app.run() 