from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State 
import yfinance as yf
from datetime import datetime

ticker_options = {'Tesla':'TSLA', 'Apple':'AAPL', 'Microsoft':'MSFT', 'Amazon':'AMZN',
                  'Google':'GOOGL', 'Pfizer': 'PFE'}

app = Dash(__name__)  

app.layout = html.Div([
    html.H1(
        children='Stock Ticker Dashboard', 
        style={"display": "flex", "justify-content": "center"}
    ),
    html.Hr(),
    html.Div([
        html.H3(
            children='Select stock symbol',
        ),
        dcc.Dropdown(
            id='my-stock-picker',
            options=[{'label': label, 
                      'value':value} for label, value in ticker_options.items()],
            value='MSFT'
        )
    ], style={'display':'inline-block'}),
    html.Div([
        html.H3(
            children='Select a date range',
        ),
        dcc.DatePickerRange(
            id='date-picker',
            min_date_allowed=datetime(2015,1,1),
            max_date_allowed=datetime.today(),
            start_date=datetime(2022,1,1),
            end_date=datetime.today(),
        )
    ], style={'display':'inline-block'}),
    html.Hr(),
    dcc.Graph(
        id='my-graph',
        figure={'data':[]},
    ),
    html.Div(id='ver')
    
])

@app.callback(Output('ver', 'children'),
              Input('date-picker', 'start_date'))
def verrr(start):
    #start = datetime.strptime(start, '%Y-%m-%d')
    return start[:10]

@app.callback(Output('my-graph', 'figure'),
              [Input('my-stock-picker', 'value'),
               Input('date-picker', 'start_date'),
               Input('date-picker', 'end_date')])
def update_graph(stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    df = yf.Ticker(stock_ticker).history(interval='1d',start=start, end=end)
    
    fig = {'data':[{'x':df.index,
                    'y':df['Close']}], 

           'layout':{'title':stock_ticker}
    }
    
    return fig

if __name__=='__main__':
    app.run_server(debug=True)