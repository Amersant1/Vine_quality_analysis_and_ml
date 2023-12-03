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

edu_base = df[:1500].copy()
test_base = df[1500:].copy()

edu_answers = edu_base["quality"]
edu_base = edu_base.iloc[:, : 11]

test_answers = test_base["quality"]
test_base = test_base.iloc[:, : 11]

test_new_answers = list()
for test in test_answers:
    new_list = [0,0,0,0,0,0]
    new_list[test-3] = 1
    test_new_answers.append(new_list)

test_new_answers = pd.DataFrame(test_new_answers)

edu_new_answers = list()
for test in edu_answers:
    new_list = [0,0,0,0,0,0]
    new_list[test-3]=1
    edu_new_answers.append(new_list)

edu_new_answers = np.array(edu_new_answers)  # Convert to numpy array
test_new_answers = np.array(test_new_answers)

# edu_new_answers = to_categorical(edu_new_answers, num_classes=6)
# test_new_answers = to_categorical(test_new_answers, num_classes=6)

flat = Flatten(input_shape=(11,))
dense = Dense(1000, activation="relu")
final = Dense(6, activation = "softmax")
model = keras.Sequential([flat,dense,final],name="number_rec")
print(model.summary())

model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])

model.fit(edu_base,edu_new_answers,batch_size=1,epochs=30,validation_split=0.2)

model.evaluate(test_base,test_new_answers)

new_list = model.predict(edu_base.head(1))
# print(new_list)
new_list = list(new_list[0])
# new_list = list(map(float,new_list.split(" ")))
print(new_list)
print(new_list.index(max(new_list))+3)
model.save('model.keras')


