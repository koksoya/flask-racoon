import threading
from flask import Flask,jsonify,request
from flask_cors import CORS
from frame import Frames
import os

ex = {
  "frame": Frames() 
}
#dsgdksjahıljasldj
app = Flask(__name__)
CORS(app)
@app.route("/predict",methods=['GET'])
def return_predicted_results():
  minSize = int(request.args.get('minSize'))
  maxSize = int(request.args.get('maxSize'))
  minRent = int(request.args.get('minRent'))
  maxRent = int(request.args.get('maxRent'))
  district = request.args.get("district")
  
  return_list = positive_stores_by_size_rent(ex["frame"].__getattribute__(district),district,minSize,maxSize,minRent,maxRent) 
  return_dict = {
                
                'url': return_list
                }
  return jsonify(return_dict)

@app.route("/",methods=['GET'])
def default():
  return "<h1> Welcome to store location predictor !!! <h1>"

def positive_stores_by_size_rent(positive_labeled_predictions,district,minSize,maxSize,minRent,maxRent):
    list_to_return = []
    for index in positive_labeled_predictions:
        element = ex["frame"].store[district][index]
        if element["size"] <= maxSize and element["size"] >= minSize and element["rent"] <= maxRent and element["rent"] >= minRent: 
                if element["url"] not in list_to_return:
                    list_to_return.append(element["url"])
    return list_to_return 

def refresh_frame():
    ex.frame = Frames()


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

if __name__ == "__main__":
    set_interval(refresh_frame,3600*24)
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
