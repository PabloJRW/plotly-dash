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

df = pd.read_csv('data/mocksurvey.csv', index_col=0)

trace1 = [go.Bar(x=df.index,
                y=df[col].values,
                name=col) for col in df.columns]

layout = go.Layout(title=' Survey Results', barmode='stack')

fig = go.Figure(data=trace1, layout=layout)
pyo.plot(fig)   