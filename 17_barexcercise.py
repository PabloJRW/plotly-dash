####
# Objective: Create a stacked bar chart from
# the file ..data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels. 
# Extra Credit: make a horizontal bar chart!
####

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/mocksurvey.csv')
print(df)
trace = [go.Bar(x=df['Unnamed: 0'],
                y=df[col]) for col in df.columns]

layout = go.Layout(barmode='stack')
fig = go.Figure(data=trace, layout=layout)
pyo.plot(trace)