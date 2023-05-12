import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/mpg.csv')

df = df.drop(df[df['horsepower']=='?'].index)
df['horsepower'] = df['horsepower'].astype('int')

trace = [go.Scatter(x=df.horsepower,
                    y=df.mpg,
                    text=df.name,
                    mode='markers',
                    marker=dict(size=2*df.cylinders,
                                color=df.cylinders))]

layout = go.Layout(title='Bubble Chart',
                   xaxis=dict(title='Horsepower'),
                   yaxis=dict(title='MPG'), 
                   hovermode='closest')
fig = go.Figure(data=trace, layout=layout)
pyo.plot(fig)