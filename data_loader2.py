from config import *
import psycopg2
import pandas as pd

conn=psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password)

channel_data = pd.read_sql_query('select * from channel_data',con=conn)
video_data = pd.read_sql_query('select * from video_data',con=conn)
joined_data = pd.read_sql_query('select * from joined_data',con=conn)
binned_data = pd.read_sql_query('select * from clean_binned_data',con=conn)

category_data = channel_data.groupby('topic_category').sum().reset_index()
sentiment_data = pd.read_csv('Database/ready_for_sql/sentiment_data.csv')

# join sentiment data videos_data
video_sentiment_data = joined_data.merge(sentiment_data, on='video_id', how='left')

