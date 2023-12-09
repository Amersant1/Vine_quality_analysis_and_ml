from controller import *


def show_data_frame():
    st.title("Red wines and their quality")
    st.header("data from dataset")
    st.dataframe(df) 