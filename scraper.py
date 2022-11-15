import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape
# data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('lang:ru until:2022-02-01 since:2021-01-01').get_items()):
    if i>10:
        break
    tweets_list2.append([tweet.date, tweet.content, tweet.user.username])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Text', 'Username'])

# Display first 5 entries from dataframe
tweets_df2.head()
