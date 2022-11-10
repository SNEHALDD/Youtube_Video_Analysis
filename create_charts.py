from data_loader2 import *
import plotly.express as px
import pandas as pd

template = 'seaborn'

fig = px.bar(category_data.sort_values('channel_view_count', ascending=False),
             x="topic_category", y="channel_view_count", title='Total Views by Category', template=template, height=600, width=1000)
fig.update_traces(marker_color='red')

fig2 = px.box(video_sentiment_data, x="topic_category", y="sentiment", template=template, 
              title='Analysis by Category', height=600, width=1200)
fig2.update_traces(marker_color='red')

fig4 = px.histogram(binned_data, x="day_of_week_published",template=template, 
                    title='Published Date', height=400, width=500)
fig4.update_traces(marker_color='red')
# reorder the days of the week
fig4.update_xaxes(categoryorder="array", categoryarray=[
                  "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

fig5 = px.histogram(binned_data, x=binned_data['published_at'].dt.hour,template=template, 
                    title='Time of Day Published', height=400, width=600)
fig5.update_traces(marker_color='red')
# rename labels
fig5.update_xaxes(ticktext=['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM'],
                  tickvals=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], tickangle=45)

fig6 = px.bar(channel_data.sort_values('channel_view_count', ascending=False).head(20), orientation='h',
                y="custom_url", x="channel_view_count", title='Top Channels', color='topic_category', template=template, height=600, width=1000)
fig6.update_layout(yaxis_categoryorder='total ascending')

