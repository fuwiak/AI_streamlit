# # https://github.com/twintproject/twint.git@origin/master#egg=twint

import streamlit as st
from streamlit.components.v1 import iframe
import pandas as pd
import twint
from collections import Counter


st.set_page_config(layout="centered", page_icon="🎓", page_title="AI")
st.title("Twitter Analysis")

c = twint.Config()

st.write("Enter the keyword you want to search for")
keyword = st.text_input("Keyword", "bitcoin")
c.Search = keyword


c.Limit = 2
twint.run.Search(c)

c.Pandas = True
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
grid_response = show_table_grid(Tweets_df)
data = grid_response['data']
selected = grid_response['selected_rows']
df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df




#configuration

# # Tweets_df.to_csv('tweets.csv')
#
# #configuration
# config = twint.Config()
# config.Search = "bitcoin"
# config.Lang = "en"
# config.Limit = 100
# # config.Since = "2019–04–29"
# # config.Until = "2020–04–29"
# config.Store_json = True
# config.Output = "bitcoin_out.json"
# #running search
# twint.run.Search(config)
