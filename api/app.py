from flask import Flask, jsonify, request,render_template,abort
from flask_cors import CORS

from controller import *
from handlers import *


app.run(host=HOST,port=PORT)
