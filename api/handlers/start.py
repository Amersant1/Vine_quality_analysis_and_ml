

from controller import *
from utils import *
import json
@app.route("/prediction",methods=["POST"])
def prediction_server():
    """json

    """
    data = request.get_json()
    print(data)
    prediction = predict(**data)
    print(prediction)
    return json.dumps(prediction)



