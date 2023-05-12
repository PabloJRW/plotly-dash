import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/2018WinterOlympics.csv')

trace0 = go.Bar(x=df.NOC,
                y=df.Gold,
                name='Gold',
                marker={'color':'#FFD700'})

trace1 = go.Bar(x=df.NOC,
                y=df.Silver,
                name='Silver',
                marker=dict(color='#9EA0A1'))

trace2 = go.Bar(x=df.NOC,
                y=df.Bronze,
                name='Bronze', 
                marker=dict(color='#CD7F32'))

data = [trace0, trace1, trace2]
layout = go.Layout(title='Medals', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)