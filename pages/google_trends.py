import time

import streamlit as st
from streamlit.components.v1 import iframe
import pandas as pd
# import plotly.express as px
# import googletrans
# from fpdf import FPDF
import base64

from pytrends.request import TrendReq

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


# sourcelang = googletrans.LANGUAGES



st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
st.title("Google Trends")

#sl select date range
col1, col2 = st.columns(2)
start_date = col1.date_input('Start date')
end_date = col2.date_input('End date')

#get date from date range

start_date = start_date.strftime("%Y-%m-%d")
end_date = end_date.strftime("%Y-%m-%d")

#date range pytrends



pytrends = TrendReq(hl='en-UK', tz=360)

if st.button("Reset"):
    st.experimental_rerun()

#select language russian or english
lang = st.selectbox("Select language", ("English", "Russian"))
if lang == "English":
    st.write("You selected English")
    pytrends = TrendReq(hl='en-US', tz=360)
else:
    st.write("You selected Russian")
    pytrends = TrendReq(hl='ru-RU', tz=360)

#randomly generated countries short codes in a list Google Language Codes





# build payload

#kw_ list as droppdown


# kw_list = ["machine learning"] # list of keywords to get data
#multi select default value
select_packages_kw = st.multiselect("Select keywords", ("machine learning", "artificial intelligence", "data science", "deep learning", "python"), default=("machine learning") )
kw_list = select_packages_kw



# kw_list = [st.text_input("Keywords:","machine learning")]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m')

#1 Interest over Time
data = pytrends.interest_over_time()
data = data.reset_index()


related_df = pytrends.related_queries()

import plotly.express as px




fig = px.line(data, x="date", y=kw_list, title='Keyword Web Search Interest Over Time')

st.plotly_chart(fig, use_container_width=True)

#show related queries in streamlit
# st.write(related_df[kw_list[0]]['top'])
# st.write(related_df[kw_list[0]]['rising'])

# col1, col2 = st.rows(2)
# col1.markdown("### top")
# AgGrid(related_df[kw_list[0]]['top'])
# col1.write(AgGrid(related_df[kw_list[0]]['top']))
# col2.markdown("### rising")
# col2.write(AgGrid(related_df[kw_list[0]]['rising']))
# AgGrid(related_df[kw_list[0]]['rising'])

data1 = related_df[kw_list[0]]['top']
gb = GridOptionsBuilder.from_dataframe(data1)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()
# pivot table always display gb

st.write("TOP")
grid_response = AgGrid(
    data1,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT',
    update_mode='MODEL_CHANGED',
    fit_columns_on_grid_load=False,
    enable_enterprise_modules=True,
    height=350,
    width='100%',
    reload_data=True
)

data = grid_response['data']
selected = grid_response['selected_rows']
df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df

data2 = related_df[kw_list[0]]['rising']
gb = GridOptionsBuilder.from_dataframe(data2)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()
# pivot table always display gb

#write rising queries
st.write("Rising queries")
grid_response = AgGrid(
    data2,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT',
    update_mode='MODEL_CHANGED',
    fit_columns_on_grid_load=False,
    enable_enterprise_modules=True,
    height=350,
    width='100%',
    reload_data=True
)

