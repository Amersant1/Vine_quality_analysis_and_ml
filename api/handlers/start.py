

from controller import *
from utils import *
from flask import Flask, jsonify, request, render_template, abort

import json
@app.route("/prediction",methods=["POST"])
def prediction_server():
    """json

    """
    try:
        print(1)
        # print(request.json)
        data = request.get_json()
        print(data)
        prediction = predict(**data)
        print(prediction)
        return json.dumps({"result":prediction})
    except Exception as err:
        print(err)
        return json.dumps(0)

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")    

