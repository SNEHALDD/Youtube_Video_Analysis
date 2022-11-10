import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import Input, Output, dcc, html
from create_charts import fig, fig2, fig4, fig5, fig6, template
from data_loader2 import (category_data, channel_data, joined_data, video_data,
                          video_sentiment_data)

app = dash.Dash(external_stylesheets=[
                dbc.themes.MATERIA], suppress_callback_exceptions=True)

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",

}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "marginLeft": "22rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}

# create a list of categories that aren't null
categories = category_data['topic_category'].unique().tolist()

# create a list of dictionaries for the dropdown
category_options = [{'label': i, 'value': i} for i in categories]

# create the sidebar
sidebar = html.Div([
    html.H3("YouTube Analysis", className='header',
            style={'color': 'red', 'textAlign': 'center'}),
    html.Hr(),
    dbc.Nav(
        [
            dbc.NavLink("Home", href="/", active="exact"),
            dbc.NavLink("Channel Category Metrics",
                        href="/page-1", active="exact"),
            dbc.NavLink("Top Channels", href="/page-5",
                        active="exact"),
            dbc.NavLink("Comment Sentiment Analysis",
                        href="/page-2", active="exact"),
            dbc.NavLink("Video Publishing Metrics",
                        href="/page-3", active="exact"),
            dbc.NavLink("Machine Learning Analysis",
                        href="/page-4", active="exact"),
            dbc.NavLink("Additional Analysis (Tableau)",
                        href="/page-6", active="exact"),
        ],
        vertical=True,
        pills=True,
    ),
],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")],
)
def render_page_content(pathname):
    # ------------------------------------------------------------
    if pathname == "/":
        return html.Div([
            dcc.Markdown('''# Youtube_Video_Analysis

![Image_Youtube_Trending](https://user-images.githubusercontent.com/106944351/199649897-df66341d-4029-40dd-b173-17aee2148b42.jpeg)

## Overview

Our goal is to create a machine learning model that will be trained to predict whether or not a youtube video has the potential to be viral. This will be based on features which include amount of subscribers that channel has, total amount of views on the channel and video, which category the video belongs to, and total amount of likes on the video. From these features, we will have over 7,000 videos to train and test this algorithm on so the model can learn which features best predict if the video will be viral. We are basing the term viral as a video that gets over 1 million views. If the video can get over 1 million views than it will be given the value of 1 which equates to viral. If the video would get less than 1 million views then it would be given the value of 0, for not viral.

We chose 1 million views as our differentiating point of viral vs. not viral. Due to a growing number of Internet and social media users, while still a big achievement, reaching that mythical million is no longer as much of a challenge. There are simply too many videos with that many views to make them all stand out. It’s safe to assume that currently, it’s better to aim at gaining at least [1 million views](https://mint.intuit.com/blog/relationships/how-much-do-youtubers-make/) to reap the benefits of going viral. If you can get 1 million views on your video that is the equivialant to about $5,000. So, to answer the question of how many views is viral - there is no simple answer here. In reality, not all viral videos are created equal, so the more views you get, the better, but for our machine learning model's sake, we chose 1 million views. 

## Contributors: 
1. Zara Khan - zaraxkhan 

2. Kevin MacDonald - macdkw89 

3. Justin Tapia - justint42 

4. Snehal Desavale - SNEHALDD 

## Resources

1. Youtube v3 API (https://www.googleapis.com/youtube/v3)
    - All data used in this project is sourced directly from the Youtube API
    - API Resources used
      - Channels
      - Comments
      - CommentThreads
      - Videos

2. Dataset Category References: 
   1. [Best Youtube Channels for every category](https://blog.hubspot.com/marketing/best-youtube-channels)
      - Using this article, we obtained each channel listed under each category for our purposes
      - We opted to not use the "Yoga" category due to its similarity to the "Fitness" category.
   2. [List of most-subscribed YouTube channels - Wikipedia](https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels)
      - Using this link, we sorted the table and grabbed the top 20 English Language channels by subscriber count for use in our analysis
      - There are a handful of duplicate channels in this data when compared to the categorical channel list mentioned above. Our analysis will drop these to avoid duplicate entries.


3. Software : 
    - Python 3.9.12
    - Scikit-learn 1.0
    - Numpy 1.21.5
    - pandas 1.4.2
    - psycopg2-binary-2.9.5
    - vaderSentiment - SentimentIntensityAnalyzer

4. Relational Database : PostgresSQL 11 connected to AWS database server. 

5. Tools / Software : Tableau public, git, pgAdmin, VS Code.
''')],)

# ------------------------------------------------------------
# Channel Category Metrics
    elif pathname == "/page-1":
        return html.Div([html.H3(children='Video Metrics by Category'),
                         html.Hr(),
                         # Container for first section
                         html.Div(className='row', style={'verticalAlign': 'top'}, children=[
                             # Container for left side of first section
                             html.Div(className='col-2', children=[
                                 # Label for selections
                                 html.H5('Select metric to view:'),
                                 # Selections
                                 dcc.RadioItems(
                                     id='xaxis', options=[
                                         {'label': ' Views',
                                             'value': 'channel_view_count'},
                                         {'label': ' Subscribers',
                                          'value': 'subscriber_count'},
                                         {'label': ' Videos',
                                             'value': 'channel_video_count'},
                                     ],
                                     value='channel_view_count',
                                     labelStyle={'display': 'block'}
                                 ),
                                 # space
                                 html.H1(''),
                                 # Label for category selection
                                 html.H5('Select categories:'),
                                 # Category selection
                                 dcc.Checklist(id='checklist',
                                               options=category_options, value=categories, labelStyle={'display': 'block'}),
                             ]),
                             # Container for right side of first section
                             html.Div(className='col-10', children=[
                                 # Graph
                                 dcc.Graph(
                                     id='bar-chart',
                                     figure=fig
                                 ),
                                 html.P('Analysis commentary:'),
                             ]),
                         ]),
                         ]
                        )

# ------------------------------------------------------------
# Comment Sentiment Analysis
    elif pathname == "/page-2":
        return html.Div([html.H3(children='Comment Sentiment Analysis by Category'),
                         html.Hr(),
                         # Container for second section
                         html.Div(className='row', children=[
                             # Container for left side of second section
                             html.Div(className='col-2', children=[
                                 # Label for selections
                                 html.H5('Select metric to view:'),
                                 # Selections
                                 dcc.RadioItems(
                                     id='xaxis', options=[
                                         {'label': ' Comment Sentiment',
                                             'value': 'sentiment'},
                                     ],
                                     value='sentiment',
                                     labelStyle={'display': 'block'}
                                 ),
                                 # space
                                 html.H1(''),
                                 # Label for category selection
                                 html.H5('Select categories:'),
                                 # Category selection
                                 dcc.Checklist(id='checklist',
                                               options=category_options, value=categories, labelStyle={'display': 'block'}),
                             ]),
                             # Container for right side of second section
                             html.Div(className='row col-10', children=[
                                 # Graph
                                 dcc.Graph(
                                     id='box-plots',
                                     figure=fig2
                                 ),
                             ])
                         ])
                         ]),
# ------------------------------------------------------------
# Video Metrics by Category
    elif pathname == "/page-3":
        return html.Div([html.H3(children='Video Pubishing Time Metrics'),
                         html.Hr(),
                         # Container for third section
                         html.Div(className='row', children=[
                             # Container for left side of third section
                             # html.Div(className='col-2', children=[
                             #   html.H5(
                             #      'Information about the charts goes here'),
                             # ]),
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
                             html.Div(className='col-4', children=[
                                 html.H5('Time of Day (CST)'),
                                 # Graph
                                 dcc.Graph(
                                     id='histogram2',
                                     figure=fig5
                                 ),
                             ])
                         ])
                         ]),
# ------------------------------------------------------------
# Machine Learning
    elif pathname == "/page-4":
        return html.Div([html.H3(children='Machine Learning Analysis'),
                         html.Hr(),
                         # Container for fourth section
                         html.Div(className='row', children=[
                             # Container for left side of fourth section
                             html.Div(children=[
                                 html.H5(
                                     'Information about ML goes here'),
                             ]),
                         ])
                         ]),
# ------------------------------------------------------------
# Top Channels
    elif pathname == "/page-5":
        return html.Div([html.H3(children='Top Channel Metrics'),
                         html.Hr(),
                         # Container for first section
                         html.Div(className='row', style={'verticalAlign': 'top'}, children=[
                             # Container for left side of first section
                             html.Div(className='col-2', children=[
                                 # Label for selections
                                 html.H5('Select metric to view:'),
                                 # Selections
                                 dcc.RadioItems(
                                     id='yaxis', options=[
                                         {'label': ' Views',
                                          'value': 'channel_view_count'},
                                         {'label': ' Subscribers',
                                          'value': 'subscriber_count'},
                                         # {'label': ' Videos',
                                         # 'value': 'channel_video_count'},
                                     ],
                                     value='channel_view_count',
                                     labelStyle={'display': 'block'}
                                 ),
                             ]),
                             # Container for right side of first section
                             html.Div(className='col-10', children=[
                                 # Graph
                                 dcc.Graph(
                                     id='top-channels',
                                     figure=fig6
                                 ),
                                 html.P(
                                     'Analysis commentary: Video Count is disabled due to bug')
                             ]),
                         ]),
                         ]
                        )
# ------------------------------------------------------------
# Tableau Dashboard
    elif pathname == "/page-6":
        # imbed tableau dashboard
        return html.Div([html.H3(children='Tableau Dashboard'),
                            html.Hr(),
                            # display tableau.html
                            html.Iframe(srcDoc=open('tableau.html', 'r').read(), width='100%', height='1000')
                            ])
# ------------------------------------------------------------
# Error404
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

@app.callback(
    Output('bar-chart', 'figure'),
    [Input('checklist', 'value'),
     Input('xaxis', 'value')],)
def update_graph(checklist, xaxis):
    filtered_df = category_data[category_data.topic_category.isin(checklist)]
    fig = px.bar(filtered_df.sort_values(xaxis, ascending=False), template=template,
                 x="topic_category", y=xaxis, title=f'Total {xaxis} by Category', height=600, width=1000)
    fig.update_traces(marker_color='red')
    return fig


@app.callback(
    Output('box-plots', 'figure'),
    [Input('checklist', 'value'),
     Input('xaxis', 'value')],)
def update_graph(checklist, xaxis):
    filtered_df = video_sentiment_data[video_sentiment_data.topic_category.isin(
        checklist)]
    fig = px.box(filtered_df, template=template,
                 x="topic_category", y=xaxis, title=f'Total {xaxis} by Category', height=600, width=1200)
    fig.update_traces(marker_color='red')
    return fig

@app.callback(
    Output('top-channels', 'figure'),
    [Input('yaxis', 'value')],)
def update_graph(yaxis):
    fig = px.bar(channel_data.sort_values(yaxis, ascending=True).tail(20), orientation='h',
                 y="custom_url", x=yaxis, title='Top Channels', color='topic_category', template=template, height=600, width=1000)
    fig.update_layout(yaxis_categoryorder='total ascending')
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
