import pandas as pd
import numpy as np
import requests
import streamlit as st


import pandas as pd
import plotly.express as px
from pandas_geojson import to_geojson
import plotly.graph_objects as go
from apps.lenta import lentaRu_parser



# Title
st.title('Новости Lenta.ru И РБК')

df = pd.read_csv('data/df.csv')

geo_json = to_geojson(df=df, lat='lat', lon='lot',
                 properties=['Location','Number of Protesters'])


center_dict = {'lat': geo_json['features'][0]['geometry']['coordinates'][0], 'lon': geo_json['features'][0]['geometry']['coordinates'][1]}

fig = px.scatter_mapbox(df, lat="lat", lon="lot", hover_name="Location", hover_data=["Number of Protesters"],
                        color_continuous_scale="Viridis", zoom=3, height=300, width=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()

# Plot!
st.plotly_chart(fig, use_container_width=True)

#LENTA
st.markdown('## Новости Lenta.ru')
st.markdown('### Последние новости')
# Задаем тут параметры
use_parser = "LentaRu"

query = st.text_input('Введите запрос', 'Протесты в Казахстане')
offset = st.number_input('Смещение', 0, 100, 0)
size = st.number_input('Количество новостей', 1, 100, 10)
sort = st.selectbox('Сортировка', ['relevance', 'date'])
title_only = st.checkbox('Только заголовки', True)
domain = st.text_input('Домен', 'lenta.ru')

material = st.number_input('Смещение', 1, 100, 1)
bloc = "4"

dateFrom_str = '2019-12-01'
dateTo_str = "2022-01-20"



dateFrom = st.date_input('Дата начала', value=pd.to_datetime(dateFrom_str))
dateTo = st.date_input('Дата окончания', value=pd.to_datetime(dateTo_str))

if use_parser == "LentaRu":
    param_dict = {'query'     : query,
                  'from'      : str(offset),
                  'size'      : str(size),
                  'dateFrom'  : dateFrom_str,
                  'dateTo'    : dateTo_str,
                  'sort'      : sort,
                  'title_only': title_only,
                  'type'      : material,
                  'bloc'      : bloc,
                  'domain'    : domain}

# print(use_parser, "- param_dict:", param_dict)

# Запускаем парсер
if st.button('Поиск'):
    if use_parser == "LentaRu":
        parser = lentaRu_parser()
        tbl = parser.get_articles(param_dict=param_dict,
                              time_step=1,
                              save_every=1,
                              save_excel=True)
    print("finish")

