import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(layout="wide", page_icon="🎓", page_title="raport_creator", initial_sidebar_state="expanded")
st.title("Create a report")

#uploading the data

uploaded_file = st.sidebar.file_uploader("Upload reviews data:", type=("csv", "xlsx"))

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

if uploaded_file is not None:
    selected_columns = st.sidebar.multiselect("Select columns to display", df.columns)
    if selected_columns:
        st.write(df[selected_columns])

#create wordcloud
if uploaded_file is not None:
    if st.sidebar.checkbox("Wordcloud"):
        from wordcloud import WordCloud
        # text = " ".join(review for review in df["review"])
        text = " ".join(review for review in df[selected_columns])
        wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
        fig, ax = plt.subplots()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(fig)

