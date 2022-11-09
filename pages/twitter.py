# # https://github.com/twintproject/twint.git@origin/master#egg=twint

import streamlit as st
from streamlit.components.v1 import iframe
import pandas as pd
import twint
from collections import Counter
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


st.set_page_config(layout="centered", page_icon="🎓", page_title="AI")
st.title("Twitter Analysis")

c = twint.Config()

st.write("Enter the keyword you want to search for")
keyword = st.text_input("Keyword", "bitcoin")
c.Search = keyword


c.Limit = 20
c.Pandas = True
twint.run.Search(c)
# twint.storage.panda.Tweets_df.to_csv('tweets.csv')


Tweets_df = twint.storage.panda.Tweets_df
# Tweets_df.to_csv('tweets.csv')

def show_table_grid(data):
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()
    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT',
        update_mode='MODEL_CHANGED',
        fit_columns_on_grid_load=False,
        enable_enterprise_modules=True,
        height=350,
        width='100%',
        reload_data=True
    )
    return grid_response


st.write("Posts")
#show df streamlit
# temp = pd.read_csv('tweets.csv')

# st.write(Tweets_df)


grid_response = show_table_grid(Tweets_df)
data = grid_response['data']
selected = grid_response['selected_rows']
df_out = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df

st.download_button(
     label="Download data as CSV",
     data=Tweets_df.to_csv().encode(),
     file_name=f'twitter_{keyword}.csv',
     mime='text/csv',
 )
