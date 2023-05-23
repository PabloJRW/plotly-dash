import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State 
import yfinance as yf
from datetime import datetime

companyList = pd.read_csv('data/NASDAQcompanylist.csv')
companyList.set_index('Symbol', inplace=True)
companyList = companyList['Name']

ticker_options = [{'label':companyList[i], 'value':i} for i in companyList.index]

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
           
    ## STOCK SYMBOL ----------
        html.Div([ 
            html.H3(
                children='Select stock symbol',
                style={'margin':'1.5px 3px', 'paddingRight':'12px'}
            ),
            dcc.Dropdown(
                id='my-stock-picker',
                options=[{'label': i.get('label'), 
                          'value':i.get('value')} for i in ticker_options],
                value='MSFT',
                multi=True, 
                style={'width':'360px', 
                       'marginRight':'12px'}
            )
        ]
        ),
    ## -----------------------------------------

    ## DATE RANGE ------------------------------
        html.Div([
            html.H3(
                children='Select a date range',
                style={'margin':'1.5px 3px', 'paddingLeft':'12px'}
            ),
            dcc.DatePickerRange(
                id='date-picker',
                min_date_allowed=datetime(2015,1,1),
                max_date_allowed=datetime.today(),
                start_date=datetime(2022,1,1),
                end_date=datetime.today(),
                style={'width':'400px',
                       'paddingLeft':'12px'}
            )
        ], 
        style={'text-align':'center','margin':'1px 3px', 'display':'inline-block', 
               'borderRight':'1px solid black', 'width':'42%'},
        ),
    ## -----------------------------------------

    ## SUBMIT BUTTON ---------------------------
        html.Div([
            html.Button(
                id='submit-button',
                n_clicks=0,
                children='Submit',
                style={'fontSize':'10px'}
            )
        ], 
        style={'display': 'flex', 'justify-content': 'center',
               'margin':'1px 1px', 'padding':'3px 3px'}
        )
    ],
    style={'display':'flex'}
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
              [Input('submit-button', 'n_clicks')],
              [State('my-stock-picker', 'value'),
               State('date-picker', 'start_date'),
               State('date-picker', 'end_date')])
def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')

    traces = []   
    if len(stock_ticker) > 1:
        for tick in stock_ticker:
            df = yf.Ticker(tick).history(interval='1d',start=start, end=end)
            traces.append({'x':df.index, 'y':df['Close'], 'name':tick})
    elif len(stock_ticker) == 1:
        df = yf.Ticker(stock_ticker[0]).history(interval='1d',start=start, end=end)
        traces.append({'x':df.index, 'y':df['Close'], 'name':tick})
        
    fig = {'data':traces, 
           'layout':{'title':stock_ticker}
    }
    
    return fig

if __name__=='__main__':
    app.run_server(debug=True)