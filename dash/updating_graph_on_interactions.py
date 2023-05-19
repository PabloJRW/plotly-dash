from dash import Dash, html, dcc 
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np

app = Dash(__name__)


df = pd.read_csv('data/mpg.csv')
#df['year'] = np.random.randint(-4, 5, len(df)) * 0.1 + df['model_year']

app.layout = html.Div([
    html.Div([
        dcc.Graph(id='mpg-scatter',
                  figure={
                      'data':[go.Scatter(x=df['model_year']+1900,
                                     y=df['mpg'],
                                     text=df['name'],
                                     hoverinfo=['all'],
                                     mode='markers')],             
                      'layout':go.Layout(title='MPG Data',
                                   xaxis={'title':'Model Year'},
                                   yaxis={'title':'MPG'},
                                   hovermode='closest')
                  }
        ),
    ], style={'width':'50%', 'display':'inline-block'}),

    html.Div([
        dcc.Graph(id='mpg-line',
                  figure={
                      'data':[go.Scatter(x=[0, 1],
                                         y=[0, 1],
                                         mode='lines')],
                      'layout':go.Layout(title='Acceleration',
                                         xaxis={'visible':False}
                                        )
                  }
        ),
    ], style={'width':'50%', 'display':'inline-block'}),
   
])


@app.callback(Output('mpg-line', 'figure'),
              [Input('mpg-scatter', 'hoverData')])
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    figure = {'data':[go.Scatter(x=[0, 1],
                                 y=[0, 60/df.iloc[v_index]['acceleration']],
                                 mode='lines'
                                 )],
              'layout':go.Layout(title=df.iloc[v_index]['name'],
                                 
                                 height=300
                                 )}
    
    return figure


if __name__=='__main__':
    app.run_server(debug=True)