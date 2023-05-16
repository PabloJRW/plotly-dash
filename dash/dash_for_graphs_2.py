import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/gapminderDataFiveYear.csv')

app = dash.Dash(__name__)

year_options = [{'label':str(year), 'value':year} for year in df['year'].unique()]
continent_options = [{'label':continent, 'value':continent} for continent in df['continent'].unique()]

app.layout = html.Div([
    dcc.Dropdown(id='year-picker',
                 options=year_options,
                 value=df['year'].min() # default value
                 ),
    dcc.Dropdown(id='continent-picker',
                 options=continent_options,
                 value='Americas'
                 ),
    dcc.Graph(id='graph-with-slider'),
])


@app.callback(
        Output('graph-with-slider', 'figure'),
        [#Input('year-picker', 'value'),
         Input('continent-picker', 'value')]
)
def update_figure(selected_year, selected_continent):
    filtered_df = df[(df['year']== selected_year) & df['continent']== selected_continent]

    traces = []
    traces.append(go.Scatter(x=filtered_df['gdpPercap'],
                             y=filtered_df['lifeExp'],
                             mode='markers',
                             text=filtered_df['country'],
                             #name=continent_name,
                             marker={'size':15},
                             opacity=0.65
                             ))
        
    
    return {
        'data':traces,
        'layout':go.Layout(
            title='My Plot',
            xaxis=dict(title='GDP per Capita'),
            yaxis=dict(title='Life Expectancy'),
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)