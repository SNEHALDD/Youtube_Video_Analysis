from dash import Dash, html, dcc, Input, Output
import plotly.express as px
from data_loader import df, joined_dff, grouped_df, video_df, sentiment_df

app = Dash(__name__)

fig = px.bar(df.sort_values('viewCount', ascending=False),
             x="video_category", y="viewCount", title='Total Views by Category', color='video_category', height=600)

fig2 = px.bar(joined_dff.sort_values('sentiment', ascending=False),
              x="topic_category", y="sentiment", title='Average Sentiment by Category', color='topic_category', height=600)

fig3 = px.bar(grouped_df.sort_values('viewCount', ascending=False),
              x="video_category", y="viewCount", title='Total Views by Category', color='video_category', height=600)

# create a list of categories that aren't null
categories = df['video_category'].unique().tolist()

# create a list of dictionaries for the dropdown
category_options = [{'label': i, 'value': i} for i in categories]

app.layout = html.Div(
    children=[
        html.H1(children='YouTube Channel Stats'),
        html.H1(children=''),
        html.Div(
            style={'display': 'flex', 'justifyContent': 'center',
                   'alignItems': 'left', 'width': '50%'},
            children=[
                # create checklist for category_type
                dcc.Checklist(
                    id='checklist',
                    options=category_options,
                    value=categories,
                ),
            ]),
        html.H1(children=''),
        html.Div(
            style={'width': '25%'},
            children=[
                html.Label('Select metric to view:'),
                # add selector for x axis
                dcc.RadioItems(
                    id='xaxis', options=[
                        {'label': 'Views', 'value': 'viewCount'},
                        {'label': 'Subscribers', 'value': 'subscriberCount'},
                        {'label': 'Videos', 'value': 'videoCount'},
                    ],
                    value='viewCount',
                )]),
        dcc.Graph(
            id='bar-chart',
            figure=fig
        ),
        dcc.Graph(
            id='bar-chart2',
            figure=fig2
        ),
        dcc.Graph(
            id='bar-chart3',
            figure=fig3
        )
    ])


@ app.callback(
    Output('bar-chart', 'figure'),
    Input('checklist', 'value'),
    Input('xaxis', 'value'))
def update_figure(selected_category, xaxis):
    # filter the data based on the selected category
    filtered_df = df[df.video_category.isin(selected_category)]
    # create the plot
    fig = px.bar(filtered_df.sort_values(xaxis, ascending=False),
                 x="video_category", y=xaxis, title='Total Views by Category', color='video_category', height=600)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
