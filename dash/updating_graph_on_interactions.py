from dash import Dash, html, dcc 
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np

app = Dash(__name__)


df = pd.read_csv('data/mpg.csv')
df['year'] = df['model_year'] + np.random.randint(-4, 5, len(df))*0.10

app.layout = html.Div([
    html.Div([
        dcc.Graph(id='mpg-scatter',
                  figure={
                      'data':[go.Scatter(
                          x=df['year']+1900,
                          y=df['mpg'],
                          text=df['name'],
                          hoverinfo='text',
                          mode='markers')],             
                      'layout':go.Layout(
                          title='MPG Data',
                          xaxis={'title':'Model Year'},
                          yaxis={'title':'MPG'},
                          hovermode='closest')
                  }
        ),
    ], style={'width':'50%', 'display':'inline-block'}),

    html.Div([
        dcc.Graph(id='mpg-line',
                  figure={
                      'data':[go.Scatter(
                          x=[0, 1],
                          y=[0, 1],
                          mode='lines')],
                      'layout':go.Layout(
                          title='Acceleration')
                  }
        ),
    ], style={'width':'50%', 'display':'inline-block'}),

    html.Div([
        dcc.Markdown(id='mpg-stats')
    ], style={'width':'20%', 'height':'50%', 'display':'inline-block'})
   
])


@app.callback(Output('mpg-line', 'figure'),
              [Input('mpg-scatter', 'hoverData')])
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    figure = {'data':[go.Scatter(x=[0, 1],
                                 y=[0, 60/df.iloc[v_index]['acceleration']],
                                 mode='lines',
                                 line={'width':df.iloc[v_index]['cylinders']*3}
                                 )],
              'layout':go.Layout(title=df.iloc[v_index]['name'].title(),
                                 xaxis={'visible':False},
                                 yaxis={'visible':False, 'range':[0,60/df['acceleration'].min()]},
                                 height=300
                                 )}
    return figure


@app.callback(Output('mpg-stats', 'children'),
              [Input('mpg-scatter', 'hoverData')])
def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
                {} cylinders 
                {} cc displacement
                0 to 60mph in {} seconds
            """.format(df.iloc[v_index]['cylinders'],
                       df.iloc[v_index]['displacement'],
                       df.iloc[v_index]['acceleration'])
    return stats

if __name__=='__main__':
    app.run_server(debug=True)