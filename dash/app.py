import dash
from dash import dcc
from dash import html

app = dash.Dash()

data0 = {'x':[1,2,3], 'y':[4,1,2]}
data1 = {'x':[1,2,3], 'y':[2,4,5]}

app.layout = html.Div(children=[
    html.H1('Hello Dash'),
    html.Div('Dash: Web Dashboards with Python'),
    dcc.Graph(id='example',
              figure={
                  'data':[
                      {'x':data0['x'], 'y':data0['y'], 'type':'bar', 'name':'SF'},
                      {'x':data1['x'], 'y':data1['y'], 'type':'bar', 'name':'NYC'}],
                  'layout':dict(
                      title='Bar Plots',
                      hovermode='closest')
              }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)