import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State 
import yfinance as yf
from datetime import datetime

ticker_options = {'Tesla':'TSLA', 'Apple':'AAPL', 'Microsoft':'MSFT', 'Amazon':'AMZN',
                  'Google':'GOOGL', 'Netflix': 'NFLX', 'Meta':'META'}

#ticker_options = [{'label':l, 'value':v} for l, v in ticker_options.items()]

app = Dash(__name__)  

app.layout = html.Div([
    html.H1(
        children='NASDAQ Stocks Dashboard', 
        style={"display": "flex", "justify-content": "center",
               'paddingTop':'1px', 'margin':'10px 0px'}
    ),
    html.Hr(
        style={'margin': '1px 0px'}
    ),
    html.Div([

    #### INICIO DIV - Contenedor de selección de opciones
    # Este DIV es el área de selección de opciones, 
    # uno de los n contenedores principales. 
    # Continene los elementos de selección para:
    #  - Stock Symbol 
    #  - Rango de fecha

           
    ## STOCK TICKER ----------
        html.Div([ 
            html.H3(
                children='Select stock symbol',
                style={'margin':'1.5px 3px', 'paddingRight':'12px'}
            ),
            dcc.Checklist(
                id='stock-picker',
                options=[{'label': l, 
                          'value': v} for l, v in ticker_options.items()],
                value=['TSLA'], 
                inline=True,
                style={'width':'300px', 
                       'marginRight':'1px',
                       'paddingTop':'6px', 
                       'paddingRight':'12px',
                       'paddingLeft':'12px',
                       'display':'flex',
                       'alignItems':'center',
                       'justifyContent':'center'
                       }
            )
        ],
        style={'width':'420px', 'borderRight':'1px solid grey'}
        ),
    ## -----------------------------------------

    ## DATE RANGE ------------------------------
        html.Div([
            html.H3(
                children='Select a date range',
                style={'margin':'1.5px 12px'}
            ),
            dcc.DatePickerRange(
                id='date-picker',
                min_date_allowed=datetime(2015,1,1),
                max_date_allowed=datetime.today(),
                start_date=datetime(2022,1,1),
                end_date=datetime.today(),
                style={'marginLeft':'24px',
                       'height':'90px',
                       'position':'absolute'}
            )
        ], 
        style={'margin':'1px 1px', 'display':'inline-block', 
               'borderRight':'1px solid grey', 'width':'321px'},
        ),
    ],
    style={'height':'72px', 'display':'flex'}
    ),
    ### FINAL DIV - contenedor de selección de opciones
    ### *********
    html.Hr(),

    ### INICIO DIV - Contenedor del gráfico
    dcc.Graph(
        id='my-graph',
        figure={'data':[]}
    )
    ### FINAL DIV - Contenedor del gráfico
    
    
])




@app.callback(Output('my-graph', 'figure'),
              [Input('stock-picker', 'value'),
               Input('date-picker', 'start_date'),
               Input('date-picker', 'end_date')])
def update_graph(stock_ticker, start_date, end_date):
    start_date = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end_date = datetime.strptime(end_date[:10], '%Y-%m-%d')

    traces = [] 
    if len(stock_ticker) > 1:
        for tick in stock_ticker:
            df = yf.Ticker(tick).history(interval='1d',start=start_date, end=end_date)
            traces.append({'x':df.index, 'y':df['Close'], 'name':tick})
    elif len(stock_ticker) == 1:
        df = yf.Ticker(stock_ticker[0]).history(interval='1d',start=start_date, end=end_date)
        traces.append({'x':df.index, 'y':df['Close']})
        
    fig = {'data':traces, 
           'layout':{'title':stock_ticker}
    }
    
    return fig

if __name__=='__main__':
    app.run_server(debug=True)