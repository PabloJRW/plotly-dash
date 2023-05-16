from dash import Dash, html, dcc 
from datetime import date

app = Dash(__name__)

provincias = ['Bocas del Toro','Coclé','Colón','Chiriquí',
                  'Darién','Herrera','Los Santos','Panamá','Veraguas']

app.layout = html.Div([
    # DROPDOWN
    html.Label('Dropdown'),
    dcc.Dropdown(id='dropdown',
                 options=provincias, 
                 value='Panamá'),
    html.Br(),

    # DROPDOWN MULTI
    html.Label('Dropdown Multi'),
    dcc.Dropdown(id='multi-dropdown',
                 options=provincias, 
                 value='Panamá', 
                 multi=True,
                 clearable=True),
    html.Br(),

    # SLIDER
    html.Label('Slider'),
    dcc.Slider(id='slider',
               min=0, 
               max=10, 
               step=1),
    html.Br(),

    # CHECKLIST
    html.Label('Checklist'),
    dcc.Checklist(id='check-list',
                  options=provincias)
])
 
if __name__ == '__main__':
    app.run_server(debug=True)