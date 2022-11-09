from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from data_loader import df, binned_df, binned_sentiment_df

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

fig = px.bar(df.sort_values('viewCount', ascending=False),
             x="video_category", y="viewCount", title='Total Views by Category', template='plotly_dark', height=600, width=1000)
fig.update_traces(marker_color='red')

# box plots for sentiment analysis in each category
fig2 = px.box(binned_sentiment_df, x="topic_category", y="sentiment", title='Analysis by Category', template='plotly_dark', height=600, width=1000)
fig2.update_traces(marker_color='red')

# 3d scatter plot
fig3 = px.scatter_3d(binned_df.groupby('topic_category').mean().reset_index(), x="channel_video_count", y="channel_view_count", z="like_count", color="topic_category", title='3D Scatter Plot', template='plotly_dark', height=600, width=1000)
fig3.update_traces(marker=dict(size=8, line=dict(width=2, color='DarkSlateGrey'), opacity=0.8))


# make a chart of the published dates for each video 
fig4 = px.histogram(binned_df, x="day_of_week_published", title='Published Date', template='plotly_dark', height=600, width=1000)
fig4.update_traces(marker_color='red')


'''channel_id,custom_url,topic_category,channel_view_count,subscriber_count,channel_video_count,video_id,published_at,video_length,like_count,comment_count,
view_count,channel_views_binned,subscribers_binned,video_count_binned,day_of_week_published,like_count_binned,comment_binned,video_views_binned'''

# create a list of categories that aren't null
categories = df['video_category'].unique().tolist()

# create a list of dictionaries for the dropdown
category_options = [{'label': i, 'value': i} for i in categories]

# The apps layout begins here

app.layout = html.Div(className='body', style={'padding': '10px'}, children=[
    # link to stylesheet
    html.Link(rel='stylesheet', href='https://codepen.io/chriddyp/pen/bWLwgP.css', type='text/css'),
    # Header
    html.H1(children='YouTube Top Channels Trend Analysis'),
    html.P(style={'color': 'white'}, children='This is a dashboard that displays data from YouTube channels.'),
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
    html.H3(children='4th Section'),
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
                id='histogram',
                figure=fig4
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
