import streamlit as st

import pandas as pd
import matplotlib.cm as cm

import numpy as np
import seaborn as sns
import matplotlib.pyplot  as plt
import random
import plotly.express as px


#------------------------------------------------------------data
path='..\data\winequality-red (1).csv'


df = pd.read_csv(path)

st.title("Red wines and their quality")
st.header("data from dataset")
st.dataframe(df) 