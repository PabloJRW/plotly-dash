from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State 
import yfinance as yf
from datetime import datetime


app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        children='Stock Ticker Dashboard'),
    html.H3(
        children='Enter a stock symbol'),
    dcc.Input(
        id='my-stock-picker',
        value='TSLA'),
    dcc.Graph(
        id='my-graph',
        figure={'data':[]}
    )
])


@app.callback(Output('my-graph', 'figure'),
              [Input('my-stock-picker', 'value')])
def update_graph(stock_ticker):
    start = datetime(2022,1,1)
    end = datetime(2022,12,31)
    df = yf.Ticker(stock_ticker).history(interval='1d',start=start, end=end)
    
    fig = {'data':[{'x':df.index,
                    'y':df.Close}], 
           'layout':{'title':stock_ticker}}
    
    return fig

if __name__=='__main__':
    app.run_server(debug=True)