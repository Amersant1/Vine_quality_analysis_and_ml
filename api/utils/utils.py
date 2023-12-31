import numpy as np
from controller import *

def predict(**data):
    """ data : fixed acidity	volatile acidity	citric acid,	residual sugar	chlorides	free sulfur dioxide	total sulfur dioxide	density	pH	sulphates	alcohol"""
    new_data = list() 
    new_data.append(float(data["fixed acidity"]))
    new_data.append(float(data["volatile acidity"]))
    new_data.append(float(data["citric acid"]))
    new_data.append(float(data["residual sugar"]))
    new_data.append(float(data["chlorides"]))
    new_data.append(float(data["free sulfur dioxide"]))
    new_data.append(float(data["total sulfur dioxide"]))
    new_data.append(float(data["density"]))
    new_data.append(float(data["ph"]))
    new_data.append(float(data["sulphates"]))
    new_data.append(float(data["alcohol"]))
    new_data = np.array([new_data])
    prediction = MODEL.predict(new_data)
    new_list = list(prediction[0])
    answer = new_list.index(max(new_list))+3
    return answer