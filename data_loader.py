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
binned_df = pd.read_csv('Database/ready_for_sql/binned_joined_data.csv')


'''channel_id,custom_url,topic_category,channel_view_count,subscriber_count,channel_video_count,video_id,published_at,video_length,like_count,comment_count,
view_count,channel_views_binned,subscribers_binned,video_count_binned,day_of_week_published,like_count_binned,comment_binned,video_views_binned'''

'''df['video_category'] = df['video_category'].replace('Classical_music', 'Music')
df['video_category'] = df['video_category'].replace('Rock_music', 'Music')
df['video_category'] = df['video_category'].replace('Pop_music', 'Music')
df['video_category'] = df['video_category'].replace('Hip_hop_music', 'Music')
df['video_category'] = df['video_category'].replace('Electronic_music', 'Music')
df['video_category'] = df['video_category'].replace('Strategy_video_game', 'Video_games')
df['video_category'] = df['video_category'].replace('Action-adventure_game', 'Video_games')
df['video_category'] = df['video_category'].replace('Video_game_culture', 'Video_games')
df['video_category'] = df['video_category'].replace('Film', 'Entertainment')
df['video_category'] = df['video_category'].replace('Television_program', 'Entertainment')
df['video_category'] = df['video_category'].replace('Physical_fitness', 'Sport')
df['video_category'] = df['video_category'].replace('Tourism', 'Lifestyle')'''


'''# change all classical_music to music
binned_df['topic_category'] = binned_df['topic_category'].replace('Classical_music', 'Music')
binned_df['topic_category'] = binned_df['topic_category'].replace('Rock_music', 'Music')
binned_df['topic_category'] = binned_df['topic_category'].replace('Pop_music', 'Music')
binned_df['topic_category'] = binned_df['topic_category'].replace('Hip_hop_music', 'Music')
binned_df['topic_category'] = binned_df['topic_category'].replace('Electronic_music', 'Music')
binned_df['topic_category'] = binned_df['topic_category'].replace('Strategy_video_game', 'Video_games')
binned_df['topic_category'] = binned_df['topic_category'].replace('Action-adventure_game', 'Video_games')
binned_df['topic_category'] = binned_df['topic_category'].replace('Video_game_culture', 'Video_games')
binned_df['topic_category'] = binned_df['topic_category'].replace('Film', 'Entertainment')
binned_df['topic_category'] = binned_df['topic_category'].replace('Television_program', 'Entertainment')
binned_df['topic_category'] = binned_df['topic_category'].replace('Physical_fitness', 'Sport')
binned_df['topic_category'] = binned_df['topic_category'].replace('Tourism', 'Lifestyle')
binned_df['topic_category'] = binned_df['topic_category'].replace('American_football', 'Sport')
binned_df['topic_category'] = binned_df['topic_category'].replace('Christian_music', 'Music')'''

# join sentiment data to binned_df
binned_sentiment_df = binned_df.merge(sentiment_df, on='video_id', how='left')

# join joined_df with sentiment_df
joined_dff = joined_df.merge(sentiment_df, on='video_id', how='left')

df = df[~df['id'].isin(random_channels)]
df = df.dropna(subset=['video_category'])
df = df.groupby('video_category').sum().reset_index()
grouped_df = df.groupby('video_category')['viewCount'].sum().reset_index()
joined_dff = joined_dff.groupby('topic_category').mean().reset_index()