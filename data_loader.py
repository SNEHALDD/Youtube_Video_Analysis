
import os
import pandas as pd
from Jupyter_Notebook_Files.yt_channels import random_channels

# load csv
def load_csv(csv_path):
    return pd.read_csv(csv_path)

# load data
df = pd.read_csv('Database/ready_for_sql/channels_data.csv')
video_df = pd.read_csv('Database/ready_for_sql/video_data.csv')
sentiment_df = pd.read_csv('Database/ready_for_sql/sentiment_data.csv')
joined_df = pd.read_csv('Database/ready_for_sql/joined_data.csv')

# join joined_df with sentiment_df
joined_dff = joined_df.merge(sentiment_df, on='video_id', how='left')

df = df[~df['id'].isin(random_channels)]
df = df.dropna(subset=['video_category'])
df = df.groupby('video_category').sum().reset_index()
grouped_df = df.groupby('video_category')['viewCount'].sum().reset_index()
joined_dff = joined_dff.groupby('topic_category').mean().reset_index()
