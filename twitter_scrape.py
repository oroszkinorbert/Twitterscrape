import xlsxwriter
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime
start_time = datetime.now()

query ="Nuclear Power Plant"
limit=10000

tweets=[]
for tweet in sntwitter.TwitterSearchScraper(f'{query} min_faves:10 since:2021-10-01 until:2023-03-10').get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.viewCount, tweet.date,  tweet.url, tweet.user.username, tweet.content, tweet.likeCount, tweet.retweetCount, tweet.replyCount, tweet.quoteCount])
        
df = pd.DataFrame(tweets, columns=['Views','Date','Url', 'User', 'Tweet', 'Like', 'Retweet', 'Reply', 'Quote'])
date_columns = df.select_dtypes(include=['datetime64[ns, UTC]']).columns
for date_column in date_columns:
    df[date_column] = df[date_column].dt.date


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
print(len(tweets))

workbook =xlsxwriter.Workbook(f'C:/Users/Norbi/Desktop/Konyvek/ProjectLab/{query}10.xlsx')
df.to_excel(f'C:/Users/Norbi/Desktop/Konyvek/ProjectLab/{query}10.xlsx',"Munka1")