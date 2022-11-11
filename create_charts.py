from data_loader import *
import plotly.express as px
import pandas as pd

template = 'seaborn'
# Channel Category Metrics
fig = px.bar(category_data.sort_values('channel_view_count', ascending=False),
             x="topic_category", y="channel_view_count", title='Total Views by Category', template=template, height=600, width=1000, labels={'topic_category':'Category', 'channel_view_count':'Total Views'})
fig.update_traces(marker_color='red')

# Sentiment Analysis
fig2 = px.box(video_sentiment_data, x="topic_category", y="sentiment", template=template, labels={'topic_category':'Category', 'sentiment':'Sentiment Score'},
              title='Analysis by Category', height=600, width=1200)
fig2.update_traces(marker_color='red')

# Day of Week
fig4 = px.histogram(binned_data, x="day_of_week_published",template=template, 
                    title='Published Date', height=400, width=500,
                    labels={'day_of_week_published': 'Day of Week'})
fig4.update_traces(marker_color='red')
fig4.update_xaxes(categoryorder="array", categoryarray=[
                  "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

# Time of Day
fig5 = px.histogram(binned_data, x=binned_data['published_at'].dt.hour,template=template, 
                    title='Time of Day Published', height=400, width=600, 
                    labels={'x':'Time of Day Published', 'y':'Number of Videos'})
fig5.update_traces(marker_color='red')
fig5.update_xaxes(ticktext=['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM'],
                  tickvals=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], tickangle=45)

# Top Channels
fig6 = px.bar(channel_data.sort_values('channel_view_count', ascending=False).head(20), orientation='h',
                y="custom_url", x="channel_view_count", title='Top Channels', color='topic_category', template=template, height=600, width=1000)
fig6.update_layout(yaxis_categoryorder='total ascending')

fig7 = px.scatter_3d(binned_data, x='view_count', y='like_count', z='comment_count', color='video_views_binned', template=template, height=800, width=1600,hover_name="custom_url" )

fig8 = px.scatter_3d(binned_data2, template=template,
                        x='view_count', y='new_length', z='video_comment_count', color='topic_category', symbol='day_of_week_published', height=600, width=1000, log_x=True, log_y=True, log_z=True, 
                        labels={'new_length': 'Video Length (seconds)', 'view_count': 'Video Views', 'sentiment': 'Sentiment Score', 'topic_category': 'Category', 'channel_title': 'Channel'},
                        hover_data=['custom_url', 'topic_category', 'view_count', 'new_length', 'video_title_clean'])
fig8.update_traces(marker=dict(size=3, line=dict(width=1, color='DarkSlateGrey')),
                      selector=dict(mode='markers'))
fig9 = px.scatter(binned_data2[binned_data2['new_length'] > 5000], x='new_length', y='video_views', template=template, title='Video Lengths vs Views', color='topic_category', height=600, width=1000, labels={'new_length':'Video Length (seconds)', 'video_views':'Views'}, log_y=True)
