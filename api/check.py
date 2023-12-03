
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot  as plt
import random
import numpy as np
import matplotlib as plt
from tensorflow.keras.datasets import mnist
from tensorflow import keras
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.utils import to_categorical
path='data\winequality-red (1).csv'


df = pd.read_csv(path)

model = keras.models.load_model("./model.keras")



values = df.values.tolist()
c=0
d=0
for row in values:
    input = row[0:11]
    quality = row[11]
    new_list = model.predict(np.array([input]),verbose=None)
    # print(new_list)
    new_list = list(new_list[0])
    # new_list = list(map(float,new_list.split(" ")))
    # print(new_list)
    answer = new_list.index(max(new_list))+3
    if answer ==quality:
        # print("OK")
        c+=1
    elif abs(answer-quality)==1:
        d+=1
    else:
        # print("NOT OKAY")
        pass
print(d)
print(c)