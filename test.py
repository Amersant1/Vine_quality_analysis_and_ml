import requests
# fixed acidity	volatile acidity	citric acid	residual sugar	chlorides	free sulfur dioxide	total sulfur dioxide	density	pH	sulphates	alcohol	quality
# fixed acidity	volatile acidity	citric acid	residual sugar	part of sugar	chlorides	free sulfur dioxide	total sulfur dioxide	sulfur dioxide	density	pH	sulphates	alcohol	quality
# 0	7.4	0.70	0.00	1.9	0.019042	0.076	11.0	34.0	23.0	0.9978	3.51	0.56	9.4	5
json = {
    "fixed acidity":7.4,
    "volatile acidity":0.70,
    "citric acid":0.00,
    "residual sugar":1.9,
    "chlorides":0.076,
    "free sulfur dioxide":11.0,
    "total sulfur dioxide":34.0,
    "density":0.9978,
    "pH":3.51,
    "sulphates":0.5,
    "alcohol":9.4,
}
req=requests.post(url = "http://127.0.0.1:5000/prediction",json = json)
print(req.content)