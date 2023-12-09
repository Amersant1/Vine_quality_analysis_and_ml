from controller import *
#-------------------------------------------------------------quality box diagrams

def show_quality_diagram():
    def box_graph_click_button(type):
        fig, ax = plt.subplots()
        print(type)
        df.plot(kind="box",column=type,by="quality",ax=ax)
        plt.xlabel('quality')
        plt.ylabel(type)
        plt.title('distribution of quality'+f' ({type})')
        # plt.show()
        st.pyplot(fig)

    st.header("Here you can see different box diagrams(click on the button under the text)")
    button_labels = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
        'chlorides', 'free sulfur dioxide', 'total sulfur dioxide','density',
        'pH', 'sulphates', 'alcohol', 'quality']
    button_type = st.selectbox('Select a type', button_labels)  # assuming df is your DataFrame
    if st.button('Generate Box Plot'):
        box_graph_click_button(button_type)