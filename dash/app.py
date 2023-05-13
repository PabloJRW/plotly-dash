import dash
from dash import dcc
from dash import html

app = dash.Dash()

data0 = {'x':[1,2,3], 'y':[4,1,2]}
data1 = {'x':[1,2,3], 'y':[2,4,5]}

colors = {'background':'#111111', 'text':'#7FDBFF'}

app.layout = html.Div(children=[
    html.H1('Hello Dash', style={'textAlign':'center',
                                 'color':colors['text']}),
    html.Div('Dash: Web Dashboards with Python'),
    dcc.Graph(id='example',
              figure={
                  'data':[
                      {'x':data0['x'], 'y':data0['y'], 'type':'bar', 'name':'SF'},
                      {'x':data1['x'], 'y':data1['y'], 'type':'bar', 'name':'NYC'}],
                  'layout':dict(
                      plot_bgcolor=colors['background'],
                      paper_bgcolor=colors['background'],
                      font={'color':colors['text']},
                      title='Bar Plots',
                      hovermode='closest')
              }
    )
], style={'backgroundColor':colors['background']})

if __name__ == '__main__':
    app.run_server(debug=True)