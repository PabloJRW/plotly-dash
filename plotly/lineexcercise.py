"""
Objective: Using the file 2010YumaAZ.csv, develop a line chart
that plots seven days worth of temperature data on one graph.
You can use a for loop to assign each day to its own trace.
"""

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/2010YumaAZ.csv')

trace = [go.Scatter(x=df['LST_TIME'].unique(),
                   y=df[df['DAY']==day]['T_HR_AVG'],
                   mode='lines',
                   name=day) for day in df['DAY'].unique()]

layout = go.Layout(title='Daily Temperature Average',
                   xaxis={'title':'Hour'},
                   yaxis={'title':'Temperature'})

fig = go.Figure(data=trace,
                layout=layout)

pyo.plot(fig)