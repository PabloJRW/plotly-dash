from dash import Dash, html, dcc  
from dash.dependencies import Input, Output, State


app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='number-in',
              value=1,
              style={'fontSize':24}),
    html.Button(id='submit-button',
                n_clicks=0,
                children='Submit',
                style={'fontSize':24}),
    html.H1(id='number-out')
])


@app.callback(Output('number-out', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('number-in', 'value')])
def output(n_clicks, number):
    return number


if __name__=='__main__':
    app.run_server(debug=True)