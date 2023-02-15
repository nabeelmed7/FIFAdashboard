import plotly.graph_objs as go
import plotly.express as px
from dash import html, dash, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style(style='darkgrid')

from ipynb.fs.full.functions import create_polarcharts, get_most_valuable, get_most_wages_paid, most_represented_countries, get_highest_agg_overall, get_highest_mean_overall, get_stat_list, get_position, get_age_clubs, get_age_countries, get_stats_mvr, messivsronaldo, cleaning, positions_league, categorizing, wages_sunburst


fifa_22 = pd.read_csv('players_22.csv', low_memory=False)


# import dash
# dash.register_page(__name__)

app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])

top = dbc.Row([    dbc.Col([        html.Img(src='https://gamingtrend.com/wp-content/uploads/2021/10/FIFA-22.jpg', height='50px', 
                                             style={'display': 'block', 'margin': 'auto'})    ], width={'size': 2, 'offset': 5}),
], style={'background-color': 'rgba(241, 229, 172)', 'padding': '10px'})

marquee_1 = html.Marquee(id = 'marquee',
                         children = 'BENZEMA WINS HIS FIRST GOLDEN BALL',
                         style = {'fontWeight':'bold', 'textAlign':'center','height':'25px','font':'25px','color':'black'})


dropdown_list = ['L. Messi', 'Cristiano Ronaldo',  'M. Salah', 'K. Benzema', 'K. Mbappé', 'R. Lewandowski', 'Neymar Jr', 'K. De Bruyne', 'H. Kane']

container = dbc.Container([
        dbc.Row([
                dbc.Col(dcc.Graph(id = 'positions_player',
    figure = positions_league(fifa_22),
    style={
                              'height': '55vh',
                              'width': '100%',
                              'margin': 'auto',
                              'padding': '0px 0px 10px 0px',
                              'background-color': 'rgb(223, 223, 223)',
                              'display': 'inline-block',
                              'border': '0.5px solid black'
                          }
        
            )),
            dbc.Col(dcc.Graph(id = 'output',
      figure = most_represented_countries(fifa_22),
                      style = {
                              'height': '55vh',
                              'width': '100%',
                              'margin': 'auto',
                              'padding': '0px 0px 10px 0px',
                              'background-color': 'rgb(223, 223, 223)',
                              'display': 'inline-block',
                              'border': '0.5px solid black'
                          }
              
            ), ),
            ],
        )
    ],
)

dropdown_row = dbc.Row(
    dbc.Col(
        dcc.Dropdown(
            id='card_dropdown',
            options=dropdown_list,
            value='Cristiano Ronaldo',
            style={
                'width': '100%',
                'margin': 'auto',
                'padding': '0px 0px 10px 0px',
                'background-color': 'rgb(241, 229, 172)',
                'margin-bottom': '-10px',
                'border': '0.5px solid black'
            }
        ),
        width=12
    )
)

graph_row = dbc.Row(
    dbc.Col(
        dcc.Graph(
            id='player_output',
            style={
                'height': '60vh',
                'width': '100%',
                'margin': 'auto',
                'padding': '0px 0px 10px 0px',
                'background-color': 'rgb(241, 229, 172)',
                'border': '0.5px solid black',
                'margin-top': '20px'
            }
        ),
        width=12
    )
)

player_dropdown = dbc.Container([    dropdown_row,    graph_row,], style={
                                                                          'text-align': 'center',
                                                                         'max-width': '750px',   # set max width to 800 pixels
                                                                        'margin': 'auto', })


wages_mvr = dbc.Container([ html.Br(),
                           html.Br(),
                           html.Br(),
        dbc.Row([
            dbc.Col(
                dcc.Graph(id = 'wages_leagues',
    figure = wages_sunburst(fifa_22),
    style={
                              'height': '55vh',
                              'width': '100%',
                              'margin': 'auto',
                              'padding': '0px 0px 10px 0px',
                              'background-color': 'rgb(223, 223, 223)',
                              'display': 'inline-block',
                              'border': '0.5px solid black'
                          }
        
            )
            ),
            dbc.Col(
                dcc.Graph(id = 'messivronaldo',
    figure = messivsronaldo(fifa_22),
    style={
                              'height': '55vh',
                              'width': '100%',
                              'margin': 'auto',
                              'padding': '0px 0px 10px 0px',
                              'background-color': 'rgb(223, 223, 223)',
                              'display': 'inline-block',
                              'border': '0.5px solid black'
                          }
        
            )
            )
        ])
    ])

ages = dbc.Container([ 
        dbc.Row([
            dbc.Col(
                dcc.Graph(id='agedistcountry',
                          figure=get_age_countries(fifa_22),
                          style={
                              'height': '55vh',
                              'width': '100%',
                              'margin': 'auto',
                              'padding': '0px 0px 10px 0px',
                              'background-color': 'rgb(223, 223, 223)',
                              'display': 'inline-block',
                              'border': '0.5px solid black'
                          }
                         )
            ),
            dbc.Col(
                dcc.Graph(id='agedistclubs',
                          figure=get_age_clubs(fifa_22),
                          style={
                              'height': '55vh',
                              'width': '100%',
                              'margin': 'auto',
                              'padding': '0px 0px 10px 0px',
                              'background-color': 'rgb(223, 223, 223)',
                              'display': 'inline-block',
                              'border': '0.5px solid black'
                          }
                         )
            )
        ])
    ])

@app.callback(
    Output(component_id = 'player_output',component_property = 'figure'),
    Input(component_id = 'card_dropdown', component_property = 'value')
)
def update_output(value):
    if value == 'L. Messi':
        return create_polarcharts(get_stat_list(fifa_22, value), 'purple', app.get_asset_url('P4aNPI-lionel-messi-football-render-footyrenders.png'), 'Messi', 'RW/CAM')
    elif value == 'Cristiano Ronaldo':
        return create_polarcharts(get_stat_list(fifa_22, value), 'white', app.get_asset_url('PngItem_985112.png'), 'Cristiano Ronaldo', 'LW/ST')
    elif value == 'M. Salah':
        return create_polarcharts(get_stat_list(fifa_22, value), 'red', app.get_asset_url('p118748.png'), 'M. Salah', 'RW')
    elif value == 'K. Benzema':
        return create_polarcharts(get_stat_list(fifa_22, value), 'gold', app.get_asset_url('benzigold.png'), 'K. Benzema', 'ST')
    elif value == 'R. Lewandowski':
        return create_polarcharts(get_stat_list(fifa_22, value), 'maroon', app.get_asset_url('lewa1.png'), 'R. Lewandowski', 'ST')
    elif value == 'Neymar Jr':
        return create_polarcharts(get_stat_list(fifa_22, value), 'yellow', app.get_asset_url('neymar-brazil-png-10.png'), 'Neymar Jr', 'LW/CAM')
    elif value == 'K. De Bruyne':
        return create_polarcharts(get_stat_list(fifa_22, value), 'light blue', app.get_asset_url('Kevin-De-Bruyne-Transparent-Free-PNG.png'), 'Kevin De Bruyne', 'CAM/CM')
    elif value == 'H. Kane':
        return create_polarcharts(get_stat_list(fifa_22, value), 'silver', app.get_asset_url('harry2.png'), 'Harry Kane', 'ST')
    else:
        return create_polarcharts(get_stat_list(fifa_22, value), 'dark blue', app.get_asset_url('Kylian-Mbappe-Footballer-PNG-Image.png'), 'K. Mbappé', 'RW/LW/ST')
    

app.layout = html.Div(id = 'parent', 
                      children = [top, marquee_1, player_dropdown, wages_mvr, container, ages],
                     style = {'background-color' : 'rgb(223, 223, 223)'})


if __name__ == "__main__":
    app.run_server(debug = False)