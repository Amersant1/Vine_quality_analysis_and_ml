import streamlit as st

import pandas as pd
import matplotlib.cm as cm

import numpy as np
import seaborn as sns
import matplotlib.pyplot  as plt
import random
import plotly.express as px


# #------------------------------------------------------------data
# path='..\data\winequality-red (1).csv'


# df = pd.read_csv(path)

# st.title("Red wines and their quality")
# st.header("data from dataset")
# st.dataframe(df) 


# # # -----------------------------------------------------------quality diagram bar chart
# # st.header("quality distribution")
# # new_df = pd.DataFrame(df.quality.value_counts()).sort_index()
# # # values = new_df.values()
# # fig, ax = plt.subplots()

# # # plotdata['pies'].plot(kind="bar", title="test")
# # new_df.plot(kind="bar", color='skyblue', edgecolor='black',ax=ax)
# # # plt.bar(list(new_df.keys()),list(new_df.values()))
# # plt.xlabel('quality')
# # plt.ylabel('number of rows')
# # plt.title('distribution of quality')
# # plt.show()
# # st.pyplot(fig)


# #-------------------------------------------------------------quality box diagrams
# def box_graph_click_button(type):
#     fig, ax = plt.subplots()
#     print(type)
#     df.plot(kind="box",column=type,by="quality",ax=ax)
#     plt.xlabel('quality')
#     plt.ylabel(type)
#     plt.title('distribution of quality'+f' ({type})')
#     # plt.show()
#     st.pyplot(fig)


# button_labels = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
#        'chlorides', 'free sulfur dioxide', 'total sulfur dioxide','density',
#        'pH', 'sulphates', 'alcohol', 'quality']
# button_type = st.selectbox('Select a type', button_labels)  # assuming df is your DataFrame
# if st.button('Generate Box Plot'):
#     box_graph_click_button(button_type)


from handlers import show_data_frame,show_dist,show_quality_diagram


show_data_frame()
show_dist()
show_quality_diagram()
