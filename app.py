from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from data_loader import df, binned_df, binned_sentiment_df

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

fig = px.bar(df.sort_values('viewCount', ascending=False),
             x="video_category", y="viewCount", title='Total Views by Category', template='plotly_dark', height=600, width=1000)
fig.update_traces(marker_color='red')

# box plots for sentiment analysis in each category
fig2 = px.box(binned_sentiment_df, x="topic_category", y="sentiment",
              title='Analysis by Category', template='plotly_dark', height=600, width=1000)
fig2.update_traces(marker_color='red')

# 3d scatter plot
fig3 = px.scatter_3d(binned_df.groupby('topic_category').mean().reset_index(), x="channel_video_count", y="channel_view_count",
                     z="like_count", color="topic_category", title='3D Scatter Plot', template='plotly_dark', height=600, width=1000)
fig3.update_traces(marker=dict(size=8, line=dict(
    width=2, color='DarkSlateGrey'), opacity=0.8))

# make a chart of the published dates for each video
fig4 = px.histogram(binned_df, x="day_of_week_published",
                    title='Published Date', template='plotly_dark', height=400, width=500)
fig4.update_traces(marker_color='red')
# reorder the days of the week
fig4.update_xaxes(categoryorder="array", categoryarray=[
                  "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])

binned_df['published_at'] = pd.to_datetime(binned_df['published_at'])
# make a chart for the time of day videos are published
fig5 = px.histogram(binned_df, x=binned_df['published_at'].dt.hour,
                    title='Time of Day Published', template='plotly_dark', height=400, width=600)
fig5.update_traces(marker_color='red')
# rename labels
fig5.update_xaxes(ticktext=['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM'],
                  tickvals=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], tickangle=45)

'''channel_id,custom_url,topic_category,channel_view_count,subscriber_count,channel_video_count,video_id,published_at,video_length,like_count,comment_count,
view_count,channel_views_binned,subscribers_binned,video_count_binned,day_of_week_published,like_count_binned,comment_binned,video_views_binned'''

# create a list of categories that aren't null
categories = df['video_category'].unique().tolist()

# create a list of dictionaries for the dropdown
category_options = [{'label': i, 'value': i} for i in categories]

# The apps layout begins here

app.layout = html.Div(className='body', style={'padding': '20px'}, children=[
    # Header
    html.H1(children='YouTube Top Channels Trend Analysis'),
    html.P(style={'color': 'white'},
           children='This is a dashboard that displays data from YouTube channels.'),
    # Line break
    html.Hr(),
    # Section title
    html.H3(children='Category Metrics'),
    # Container for first section
    html.Div(className='row', style={'color': 'white', 'vertical-align': 'top'}, children=[
        # Container for left side of first section
        html.Div(className='col-2', children=[
            # Label for selections
            html.H5('Select metric to view:'),
            # Selections
            dcc.RadioItems(
                id='xaxis', options=[
                    {'label': 'Views', 'value': 'viewCount'},
                    {'label': 'Subscribers', 'value': 'subscriberCount'},
                    {'label': 'Videos', 'value': 'videoCount'},
                ],
                value='viewCount',
            ),
            # space
            html.H1(''),
            # Label for category selection
            html.H5('Select category to view:'),
            # Category selection
            dcc.Checklist(id='checklist',
                          options=category_options, value=categories),
        ]),
        # Container for right side of first section
        html.Div(className='col-10', children=[
            # Graph
            dcc.Graph(
                id='bar-chart',
                figure=fig
            ),
            html.P('Analysis commentary goes here')
        ]),
    ]),
    # Line break
    html.Hr(),
    # Section title
    html.H3(children='Comment Sentiment Analysis by Category'),
    # Container for second section
    html.Div(className='row', style={'color': 'white'}, children=[
        # Container for left side of second section
        html.Div(className='col-2', children=[
            html.H5('Something new goes here'),
        ]),
        # Container for right side of second section
        html.Div(className='col-10', children=[
            # Graph
            dcc.Graph(
                id='box-plots',
                figure=fig2
            ),
        ])
    ]),
    # Line break
    html.Hr(),
    # Section title
    html.H3(children='3rd Section'),
    # Container for third section
    html.Div(className='row', style={'color': 'white'}, children=[
        # Container for left side of third section
        html.Div(className='col-2', children=[
            html.H5('Something new goes here'),
        ]),
        # Container for right side of third section
        html.Div(className='col-10', children=[
            html.H5('Something new goes here'),
            # Graph
            dcc.Graph(
                id='3d-scatter',
                figure=fig3
            ),
        ])
    ]),
    # Line break
    html.Hr(),
    # Section title
    html.H3(children='Analysis of When Videos are Published'),
    # Container for third section
    html.Div(className='row', style={'color': 'white'}, children=[
        # Container for left side of third section
        html.Div(className='col-2', children=[
            html.H5('Information about the charts goes here'),
        ]),
        # Container for right side of 4th section
        html.Div(className='col-4', children=[
            html.H5('Day of Week'),
            # Graph
            dcc.Graph(
                id='histogram',
                figure=fig4
            ),
        ]),
        # Container for right side of 4th section
        html.Div(className='col-6', style={'padding': '100px'}, children=[
            html.H5('Time of Day'),
            # Graph
            dcc.Graph(
                id='histogram2',
                figure=fig5
            ),
        ])
    ]),
]
)

@ app.callback(
    Output('bar-chart', 'figure'),
    Input('checklist', 'value'),
    Input('xaxis', 'value'))
def update_figure(selected_category, xaxis):
    filtered_df = df[df.video_category.isin(selected_category)]
    fig = px.bar(filtered_df.sort_values(xaxis, ascending=False),
                 x="video_category", y=xaxis, title=f'Total {xaxis} by Category', template='plotly_dark', height=600, width=1000)
    fig.update_traces(marker_color='red')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
