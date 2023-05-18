from dash import Dash, html, dcc 
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('data/mpg.csv')

app = Dash(__name__)

features = df.columns

app.layout = html.Div([
    html.Div([
        html.Label('X Axis'),
        dcc.Dropdown(id='xaxis',
                     options=[{'label': i, 'value': i} for i in features],
                     value='displacement')
    ], style={'width':'48%', 'display':'inline-block'}),
    
    html.Div([
        html.Label('Y Axis'),
        dcc.Dropdown(id='yaxis',
                     options=[{'label': i, 'value': i} for i in features],
                     value='mpg')
    ], style={'width':'48%', 'display':'inline-block'}),
    
    dcc.Graph(id='feature-graphic')
], style={'padding':10})

@app.callback(
    Output('feature-graphic', 'figure'),
    [Input('xaxis', 'value'),
     Input('yaxis', 'value')]
)
def update_graph(xaxis_name, yaxis_name):
    return {'data':[go.Scatter(x=df[xaxis_name],
                               y=df[yaxis_name],
                               mode='markers',
                               marker={'size':15, 'opacity':0.6}
                            )
                   ], 
            'layout':go.Layout(title='My Dashboard',
                                             xaxis={'title':xaxis_name.upper()},
                                             yaxis={'title':yaxis_name.upper()},
                                             hovermode='closest'
                                             )}

if __name__=='__main__':
    app.run_server(debug=True)