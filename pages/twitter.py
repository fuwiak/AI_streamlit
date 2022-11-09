# # https://github.com/twintproject/twint.git@origin/master#egg=twint

import streamlit as st
from streamlit.components.v1 import iframe
import pandas as pd
import twint
from collections import Counter


st.set_page_config(layout="centered", page_icon="🎓", page_title="AI")
st.title("Twitter Analysis")



#
# # c = twint.Config()
# # c.Search = '#blacklivesmatter'
# # c.Limit = 2
# # twint.run.Search(c)
# #
# # c.Pandas = True
# # Tweets_df = twint.storage.panda.Tweets_df
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
