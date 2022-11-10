import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import plotly.express as px
from app import fig, fig2, fig3, fig4, fig5, df

app = dash.Dash(external_stylesheets=[
                dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "22rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
# create a list of categories that aren't null
categories = df['video_category'].unique().tolist()

# create a list of dictionaries for the dropdown
category_options = [{'label': i, 'value': i} for i in categories]
sidebar = html.Div(
    [
        html.H2("YouTube Analysis", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Channel Category Metrics",
                            href="/page-1", active="exact"),
                dbc.NavLink("Comment Sentiment Analysis",
                            href="/page-2", active="exact"),
                dbc.NavLink("Video Metrics", href="/page-3", active="exact"),
                dbc.NavLink("Machine Learning Analysis",
                            href="/page-4", active="exact"),
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
        return html.P("This is the content of the home page!")
# ------------------------------------------------------------
    elif pathname == "/page-1":
        return html.Div([html.H3(children='Video Metrics by Category'),
                         # Container for first section
                         html.Div(className='row', style={'vertical-align': 'top'}, children=[
                             # Container for left side of first section
                             html.Div(className='col-2', children=[
                                 # Label for selections
                                 html.H5('Select metric to view:'),
                                 # Selections
                                 dcc.RadioItems(
                                     id='xaxis', options=[
                                         {'label': ' Views', 'value': 'viewCount'},
                                         {'label': ' Subscribers',
                                          'value': 'subscriberCount'},
                                         {'label': ' Videos',
                                             'value': 'videoCount'},
                                     ],
                                     value='viewCount',
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
                                 html.P('Analysis commentary goes here')
                             ]),
                         ]),
                         ]
                        )

# ------------------------------------------------------------
    elif pathname == "/page-2":
        return html.Div([html.H3(children='Comment Sentiment Analysis by Category'),
                         # Container for second section
                         html.Div(className='row', children=[
                             # Container for left side of second section
                             html.Div(className='col-2', children=[
                                 html.H5('Something new goes here'),
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
    elif pathname == "/page-3":
        return html.Div([html.H3(children='Video Metrics by Category'),
                         # Container for third section
                         html.Div(className='row', children=[
                             # Container for left side of third section
                             html.Div(className='col-2', children=[
                                 html.H5(
                                     'Information about the charts goes here'),
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
                             html.Div(className='col-4', children=[
                                 html.H5('Time of Day'),
                                 # Graph
                                 dcc.Graph(
                                     id='histogram2',
                                     figure=fig5
                                 ),
                             ])
                         ])
                         ]),
# ------------------------------------------------------------
    elif pathname == "/page-4":
        return html.Div([html.H3(children='Machine Learning Analysis'),
                         # Container for fourth section
                         html.Div(className='row', children=[
                             # Container for left side of fourth section
                             html.Div(children=[
                                 html.H5(
                                     'Information about ML goes here'),
                             ]),
                         ])
                         ])
# ------------------------------------------------------------

    # If the user tries to reach a different page, return a 404 message
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
    filtered_df = df[df.video_category.isin(checklist)]
    fig = px.bar(filtered_df.sort_values(xaxis, ascending=False),
                 x="video_category", y=xaxis, title=f'Total {xaxis} by Category', template='plotly_dark', height=600, width=1000)
    fig.update_traces(marker_color='red')
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
