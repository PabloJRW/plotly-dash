import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/gapminderDataFiveYear.csv')

app = dash.Dash(__name__)

year_options = [{'label':str(year), 'value':year} for year in df['year'].unique()]

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Dropdown(id='continent-picker',
                 options=year_options,
                 value=df['year'].min() # default value
                 ),

])


@app.callback(
        Output('graph-with-slider', 'figure'),
        [Input('year-picker', 'value')]
)
def update_figure(selected_year):
    filtered_df = df[df['year']== selected_year]

    traces = []
    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent']==continent_name]
        traces.append(go.Scatter(x=df_by_continent['gdpPercap'],
                                 y=df_by_continent['lifeExp'],
                                 mode='markers',
                                 text=df_by_continent['country'],
                                 name=continent_name,
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