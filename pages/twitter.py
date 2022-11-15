
import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import snscrape.modules.twitter as sntwitter

st.set_page_config(layout="centered", page_icon="🎓", page_title="AI")
st.title("Twitter Analysis")

if st.button("Reset"):
    st.experimental_rerun()

#reset IP address to avoid getting banned streamlit



st.write("Enter the keyword you want to search for")
keyword = st.text_input("Keyword", "bitcoin")

st.write("Enter the number of tweets you want to search for")
limit = st.number_input("Limit", 5)
tweets_list2 = []
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lang:ru until:2022-02-01 since:2021-01-01').get_items()):
    if i>limit:
        break
    tweets_list2.append([tweet.date, tweet.content, tweet.user.username])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Text', 'Username'])



#save to csv button
if st.button("Save to CSV"):
    data = tweets_df2
    data.to_csv(f'{keyword}_tweets.csv', index=False)
    st.write("Downloaded")


Tweet = tweets_df2


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


grid_response = show_table_grid(tweets_df2)
data = grid_response['data']
selected = grid_response['selected_rows']
df_out = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df

st.download_button(
     label="Download data as CSV",
     data=tweets_df2.to_csv().encode(),
     file_name=f'twitter_{keyword}.csv',
     mime='text/csv',
 )
