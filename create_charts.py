from data_loader import *
import plotly.express as px
import pandas as pd

template = 'plotly_dark'
# Channel Category Metrics
fig = px.bar(category_data_new.sort_values('channel_view_count', ascending=False),
             x="topic_category", y="channel_view_count", title='Total Views by Category', template=template, height=600, width=1000, labels={'topic_category':'Category', 'channel_view_count':'Total Views'})


# Sentiment Analysis
fig2 = px.box(video_sentiment_data, x="topic_category", y="sentiment", template=template, labels={'topic_category':'Category', 'sentiment':'Sentiment Score'},
              title='Analysis by Category', height=500, width=1000)
fig2.update_traces(marker_color='red')
#px.defaults.color_continuous_scale = px.colors.sequential.thermal
# Day of Week
fig4 = px.histogram(binned_data, x="day_of_week_published",template=template, 
                    title='Published Date', height=500, width=500, color='video_views_binned',
                    category_orders={'video_views_binned': [
                        'less than 100 views', 'less than 1000 views', '1,000-10,000 views', '10,000-50,000 views', '50,000-500,000', '500,000- 1 million views', 'over 1 million views', 'over 5 million views', 'over 1 billion views']},
                    color_discrete_sequence=px.colors.sequential.thermal,
                    labels={'day_of_week_published': 'Day of Week', 'video_views_binned': 'Video Views'})
fig4.update_xaxes(categoryorder="array", categoryarray=[
                  "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

# Time of Day
fig5 = px.histogram(binned_data, x=binned_data['published_at'].dt.hour,template=template, 
                    title='Time of Day Published', height=500, width=600, color='video_views_binned', 
                    category_orders={'video_views_binned': [
                        'less than 100 views', 'less than 1000 views', '1,000-10,000 views', '10,000-50,000 views', '50,000-500,000', '500,000- 1 million views', 'over 1 million views', 'over 5 million views', 'over 1 billion views']},
                    color_discrete_sequence=px.colors.sequential.thermal,
                    labels={'x':'Time of Day Published', 'y':'Number of Videos', 'video_views_binned':'Video Views'})

fig5.update_xaxes(ticktext=['12AM',  '2AM',  '4AM',  '6AM',  '8AM', '10AM',  '12PM',  '2PM', '4PM', '6PM', '8PM',  '10PM', ],
                  tickvals=[0, 2, 4,  6,  8,  10,  12,  14,  16,  18, 20,  22, ], tickangle=45)

# Top Channels
fig6 = px.bar(mega_df3.sort_values('view_count', ascending=False).head(20), orientation='h',
                y="custom_url", x="view_count", title='Top Channels', color='topic_category', template=template, height=600, width=1000)
fig6.update_layout(yaxis_categoryorder='total ascending')

fig7 = px.scatter_3d(binned_data, x='view_count', y='like_count', z='comment_count', color='video_views_binned', template=template, height=800, width=1600,hover_name="custom_url" )

fig8 = px.scatter_3d(mega_df2, template=template,
                            x='view_count', y='video_length_seconds', z='comment_count', color='topic_category' ,symbol='day_of_week_published', height=800, width=1000, log_x=True, log_y=True, log_z=True,
                            labels={'video_length_seconds': 'Video Length (seconds)', 'topic_category': 'Category', 'view_count': 'Video Views', 'comment_count': "Number of Video Comments",
                                    'topic_category': 'Category', 'channel_title': 'Channel', 'day_of_week_published': 'Day of Week Published'},
                            hover_data=['custom_url', 'topic_category', 'view_count', 'video_length_seconds'])

fig8.update_layout(
    margin=dict(l=0,r=0,b=0,t=0),
    paper_bgcolor="Black"
    )
fig8.update_traces(marker=dict(size=3, line=dict(width=1, color='DarkSlateGrey')),
                      selector=dict(mode='markers'))


fig9 = px.scatter(binned_data2, x='new_length', y='video_views', 
    template=template, title='Video Lengths vs Views', color='topic_category', height=600, width=1000, 
    labels={'new_length':'Video Length (seconds)', 'video_views':'Views', 'topic_category': 'Category'}, log_y=True, log_x=True, hover_data=['custom_url', 'topic_category', 'view_count'])
fig9.update_traces(
    # change marker size
    marker=dict(size=5, line=dict(width=1, color='DarkSlateGrey')),
)


