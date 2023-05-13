import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# Creating data
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div([
    dcc.Graph(
        id='scatterplot', 
        figure={'data':[go.Scatter(x=random_x,
                                   y=random_y,
                                   mode='markers',
                                   marker=dict(
                                       size=12,
                                       color='rgb(51, 204, 153)',
                                       symbol='hexagon',
                                       line={'width':1.5}
                                    ))
                        ], 

                'layout':go.Layout(title='My Scatterplot',
                                   xaxis=dict(title='random_x'),
                                   yaxis=dict(title='random_y')
                                   )
        }
    ),


    dcc.Graph(
        id='scatterplot', 
        figure={'data':[go.Scatter(x=random_x,
                                   y=random_y,
                                   mode='markers',
                                   marker=dict(
                                       size=12,
                                       color='rgb(230, 104, 113)',
                                       symbol='pentagon',
                                       line={'width':1.5}
                                    ))
                        ], 

                'layout':go.Layout(title='My Scatterplot 2',
                                   xaxis=dict(title='random_x'),
                                   yaxis=dict(title='random_y')
                                   )
        }
    ) 
])

if __name__ == '__main__':
    app.run_server(debug=True)