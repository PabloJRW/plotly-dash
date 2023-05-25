import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State 
import yfinance as yf
from datetime import datetime

ticker_options = {'Tesla':'TSLA', 'Apple':'AAPL', 'Microsoft':'MSFT', 'Amazon':'AMZN',
                  'Google':'GOOGL', 'Netflix': 'NFLX', 'Meta':'META'}

interval_options = ['1h','1d','1wk','1mo','3mo']

#ticker_options = [{'label':l, 'value':v} for l, v in ticker_options.items()]

app = Dash(__name__, external_stylesheets=['styles.css'])  

app.layout = html.Div([
    html.H1(  
        id='header',
        children='NASDAQ Stocks Dashboard', 
        style={"display": "flex", "justify-content": "center",
               'padding':'18px', 'margin':'1px 0px', 'backgroundColor':'#F7931A',
               'color':'#00FF00'}
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
                id='stock-ticker-picker',
                options=[{'label': l, 
                          'value': v} for l,v in ticker_options.items()],
                value=['AAPL'], 
                inline=True,
                style={
                       'marginRight':'1px',
                       'paddingTop':'6px', 
                       'paddingRight':'12px',
                       'paddingLeft':'12px',
                       'display':'flex',
                       'alignItems':'start' 
                       }
            )  
        ],
        style={'width':'420px', 'height':'69px','marginRight':'6px', 
               'border':'1px solid #D9D2D0', 'backgroundColor':'#F7F7F7'}
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
                start_date=datetime(2019,1,1),
                end_date=datetime.today(),
                style={'marginLeft':'24px',
                       'height':'10px',
                       }
            )
        ], 
        style={'width':'321px' ,'height':'69px', 'display':'inline-block', 
               'marginRight':'6px', 'border':'1px solid #D9D2D0', 'backgroundColor':'#F7F7F7'},
        ),

    ### INICIO DIV - selector de intervalo 
        html.Div([ 
            html.H3(
                children='Select interval',
                style={'margin':'1.5px 3px', 'paddingRight':'12px'}
            ),
            dcc.Checklist(
                id='interval-selector',
                options=[{'label':i,
                          'value':i} for i in interval_options],
                value=['1d'], 
                inline=True,
                style={ 
                       'marginRight':'1px',
                       'paddingTop':'6px', 
                       'paddingRight':'12px',
                       'paddingLeft':'12px',
                       'display':'flex',
                       #'alignItems':'center' 
                       }
            )  
        ],
        style={'width':'420px', 'height':'69px','marginRight':'6px', 
               'border':'1px solid #D9D2D0', 'backgroundColor':'#F7F7F7'}
        ),
    ],
    style={'height':'72px', 'display':'flex', 'backgroundColor':'F7F7F7',
           'justifyContent':'start', 'marginButton':'12px '}
    ),
    ### FINAL DIV - contenedor de selección de opciones
    ### *********
    
    html.Hr(style={'marginTop':'0px'}),

    ### INICIO DIV - Contenedor del gráfico
    dcc.Graph(
        id='my-graph',
        figure={'data':[]}
    ),
    ### FINAL DIV - Contenedor del gráfico
    
], style={'margin':'0px 0px'})


@app.callback(Output('my-graph', 'figure'),
              [Input('stock-ticker-picker', 'value'),
               Input('date-picker', 'start_date'),
               Input('date-picker', 'end_date'),
               Input('interval-selector', 'value')])
def update_graph(stock_ticker, start_date, end_date, interval):
    start_date = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end_date = datetime.strptime(end_date[:10], '%Y-%m-%d')

    traces = [] 
    if len(stock_ticker) > 1:
        for tick in stock_ticker:
            df = yf.Ticker(tick).history(interval='1d', 
                                         start=start_date, 
                                         end=end_date)
            traces.append({'x':df.index, 'y':df['Close'], 
                           'name':tick})
    elif len(stock_ticker) == 1:
        df = yf.Ticker(stock_ticker[0]).history(interval='1d',
                                                start=start_date, 
                                                end=end_date)
        traces.append({'x':df.index, 'y':df['Close'], 
                       'name':stock_ticker})
        
    fig = {'data':traces, 
           'layout':{'title':stock_ticker}
    }
    
    return fig

if __name__=='__main__':
    app.run_server(debug=True)