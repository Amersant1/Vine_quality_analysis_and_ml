from flask import Flask, jsonify, request,render_template,abort
from flask_cors import CORS
import keras
import sys
app = Flask(__name__,static_folder="static")
CORS(app)
if sys.platform == 'win32':
    HOST = '0.0.0.0'
    PORT = 5000
else:
    HOST = '0.0.0.0'
    PORT = '80'


MODEL =keras.models.load_model("./model.keras")
