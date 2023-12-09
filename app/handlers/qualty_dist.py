# -----------------------------------------------------------quality diagram bar chart
from controller import *

def show_dist():
    st.header("quality distribution")
    new_df = pd.DataFrame(df.quality.value_counts()).sort_index()
    # values = new_df.values()
    fig, ax = plt.subplots()

    # plotdata['pies'].plot(kind="bar", title="test")
    new_df.plot(kind="bar", color='skyblue', edgecolor='black',ax=ax)
    # plt.bar(list(new_df.keys()),list(new_df.values()))
    plt.xlabel('quality')
    plt.ylabel('number of rows')
    plt.title('distribution of quality')
    plt.show()
    st.pyplot(fig)