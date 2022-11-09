from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from data_loader import df

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

fig = px.bar(df.sort_values('viewCount', ascending=False),
             x="video_category", y="viewCount", title='Total Views by Category', color='video_category', template='plotly_dark', height=600, width=800)


# graph should be full size
fig.update_layout(
    autosize=True,
)

# create a list of categories that aren't null
categories = df['video_category'].unique().tolist()

# create a list of dictionaries for the dropdown
category_options = [{'label': i, 'value': i} for i in categories]

app.layout = html.Div(className='body', style={'padding': '10px'}, children=[
    html.Link(rel='stylesheet',
                  href='https://codepen.io/chriddyp/pen/bWLwgP.css', type='text/css'),
    # Header
    html.H1(children='YouTube Data Analysis'),
    # Line break
    html.Hr(),
    # Section title
    html.H3(children='Category Metrics'),
    # Container for first section
    html.Div(className='row', style={'color': 'white'}, children=[
        # Container for left side of first section
        html.Div(className='col-4', children=[
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
        html.Div(className='col-8', children=[
            # Graph
            dcc.Graph(
                id='bar-chart',
                figure=fig
            ),
        ])
    ]
    ),
    # Line break
    html.Hr(),
    # Section title
    html.H3(children='Sentiment Analysis'),
    # Container for second section
    html.Div(className='row', style={'color': 'white'}, children=[
        # Container for left side of second section
        html.Div(className='col-4', children=[
            html.H5('Something new goes here'),
        ]),
        # Container for right side of second section
        html.Div(className='col-8', children=[
            # Graph
            dcc.Graph(
                id='bar-chart2',
                figure=fig
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
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
