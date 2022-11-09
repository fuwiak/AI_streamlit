import pandas as pd
import numpy as np
import requests
import streamlit as st

import pandas as pd
import plotly.express as px
from pandas_geojson import to_geojson
import plotly.graph_objects as go

# Title
st.title('My first app')

df = pd.read_csv('Kazachstan_dataset.csv', sep=',')

#extract float values from the column Latitude
df['lat'] = df['Latitude'].str.extract('(\d+\.\d+)', expand=False).astype(float)

df['lot'] = df['Longitude'].str.extract('(\d+\.\d+)', expand=False).astype(float)
df["Number of Protesters"].fillna(0, inplace = True)
df["Number of Protesters"] = df["Number of Protesters"].replace("Unknown", 0)
df["Number of Protesters"] = df["Number of Protesters"].astype(int)

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
