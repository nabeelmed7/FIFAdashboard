import plotly.graph_objs as go
import plotly.express as px
from dash import html, dash, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style(style='darkgrid')

import os
import pandas as pd
from glob import glob
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.graph_objs as go
import plotly.express as px
from dash import html, dash, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
sns.set_style(style='darkgrid')

fifa_22 = pd.read_csv('players_22.csv', low_memory=False)

def most_represented_countries(df):
    countries = df['nationality_name'].value_counts().nlargest(10)
    fig = px.pie(countries, values = countries, names = countries.index)
    fig.update_layout(plot_bgcolor="rgb(241, 229, 172)", paper_bgcolor="rgb(241, 229, 172)",title=f'<b>                          Most represented countries</b>',
#                      shapes=[go.layout.Shape(
#     type='rect',
#     xref='paper',
#     yref='paper',
#     x0=-0.11,
#     y0=-0.13,
#     x1=1.25,
#     y1=1.15,
#     line={'width': 1, 'color': 'black'}
#     )]
                     )
    return fig
  
  
def create_polarcharts(
    stats: list,
    color: str,
    img_link: str,
    name_one: str,
    name_two: str
):

  # Determine the number of rows and columns
  fig = make_subplots(rows=1, cols=2, 
                      # We indicate the types of graphs in each block
                      specs=[[{'type': 'xy'}, {"type": "polar"}]], 
                      # Setting the width of each column
                      column_widths=[0.5, 0.5])  

  # Create a Polar Chart
  fig.add_trace(go.Scatterpolar(
                   # Passing numeric parameters
                   r=stats,
                   # Passing parameter names
                   theta=['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physic', 'Pace'],
                   # Setting the fill parameter
                   fill='toself',
                   # Specify the signature on hover
                   hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}',
                   # Specify a caption for the legend
                   name='',
                   # Specifying the line color
                   line=dict(color=color)),
                   # Specify line and column numbers
                   row=1, col=2)

  # Add an image to the chart
  fig.layout.images = [dict(
             # Passing a link to the image
             source=img_link,
             # Specify the position of the image along the x-axis
             x=0.1, 
             # Specify the position of the image along the y-axis
             y=0.5,
             # Setting the size of the chart
             sizex=1, 
             sizey=1.2,
             # Setting the position along the x-axis
             xanchor="center", 
             # Setting the y-axis position
             yanchor="middle",
             # Place the image under the chart
             layer="below"
                           )
                      ]

  fig.update_layout(
#         shapes=[go.layout.Shape(
#         type='rect',
#         xref='paper',
#         yref='paper',
#         x0=-0.11,
#         y0=-0.13,
#         x1=1.15,
#         y1=1.35,
#         line={'width': 1, 'color': 'black'}
#         )],
       width=600,
       height=400,
      # Set the name of the chart
      title=f'<b>                                      {name_one}</b><br><sub>                                                        {name_two}</sub>',
      # Setting the background color
      paper_bgcolor="rgb(241, 229, 172)",
      # Setting the chart theme
      template='xgridoff',
      # Passing chart parameters
      polar=dict(
           # Background color
           bgcolor="rgb(241, 229, 172)",
           # Adding a line with numeric divisions
           radialaxis=dict(
                      # Displaying the line
                      visible = True,
                      # Set the range of divisions
                      range = [0, 100]
                          )
                 ), 
      # Passing the parameters to the font
      font=dict(
                # Font type
                family='Arials',
                # Font size
                size=14,
                # Font color
                color='Black'
               )
  )

  # Displaying the graph
  return fig
  
  
def get_stat_list(df, player):
  stat_list = df.loc[df['short_name'] == player][['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']].values.tolist()[0]
  return stat_list
  
def get_position(df, player):
  position = df.loc[df['short_name'] == player][['player_positions']].iloc[0].values[0]
  return position
  
def get_age_clubs(df):
  top_club_names = ('FC Barcelona','Real Madrid', 'Juventus', 'Paris Saint-Germain', 'Chelsea', 'Manchester City', 'Manchester United')
  clubs = df.loc[df['club_name'].isin(top_club_names) & df['age']]

  fig = px.box(clubs, x="club_name", y="age", color="club_name")
  fig.update_layout(
  width=600,
  plot_bgcolor="rgb(241, 229, 172)",
  paper_bgcolor="rgb(241, 229, 172)",
  title=f'<b>                   Age distribution in top clubs</b>',
  xaxis_title="Clubs",
  yaxis_title="Age",
  showlegend=False,
#     shapes=[go.layout.Shape(
#     type='rect',
#     xref='paper',
#     yref='paper',
#     x0=-0.17,
#     y0=-0.3,
#     x1=1.15,
#     y1=1.15,
#     line={'width': 1, 'color': 'black'}
#     )]
  )
  return fig
  
def get_age_countries(df):
  countries_names = ('France', 'Brazil', 'Germany', 'Belgium', 'Spain', 'Netherlands', 'Argentina', 'Portugal', 'Chile', 'Colombia')
  countries = df.loc[df['nationality_name'].isin(countries_names) & df['age']]

  fig = px.box(countries, x="nationality_name", y="age", color="nationality_name")
  fig.update_layout(
  width=600,
  plot_bgcolor="rgb(241, 229, 172)",
  paper_bgcolor="rgb(241, 229, 172)",
  title=f'<b>                   Age distribution in top countries</b>',
  xaxis_title="Clubs",
  yaxis_title="Age",
  showlegend=False,
#     shapes=[go.layout.Shape(
#     type='rect',
#     xref='paper',
#     yref='paper',
#     x0=-0.17,
#     y0=-0.22,
#     x1=1.15,
#     y1=1.15,
#     line={'width': 1, 'color': 'black'}
#     )]
  )
  return fig
  
def get_stats_mvr(df, player):
  stat_list = df.loc[df['short_name'] == player][['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 'pace']].values.tolist()[0]
  return stat_list
  
def messivsronaldo(df):
  fig = make_subplots(rows=1, cols=3, 
                  specs=[[{'type': 'xy'}, {"type": "polar"}, {'type': 'xy'},]],
                  column_widths=[0.1, 0.3, 0.1])

  fig.add_trace(go.Scatterpolar(
           r=get_stats_mvr(df, 'L. Messi'),
           theta=['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physic', 'Pace'],
           fill='toself',
           hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}',
           showlegend=True,
           name='Ronaldo',
           line=dict(
                     color='Black'
                     )
  ),
           row=1, col=2)

  fig.add_trace(go.Scatterpolar(
           r=get_stats_mvr(df, 'Cristiano Ronaldo'),
           theta=['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physic', 'Pace'],
           fill='toself',
           hovertemplate='<b>%{theta}</b>' + f'<b>: '+'%{r}',
           showlegend=True,
           name='Messi',
           line=dict(
                     color='MidnightBlue'
                     )
  ),
           row=1, col=2)


  fig.layout.images = [dict(
          source="https://1vs1-7f65.kxcdn.com/img/players/players/lionel-andres-messi_1548_56-ub-800.webp",
          xref="paper", 
          yref="paper",
          x=0.97, 
          y=0.5,
          sizex=1, 
          sizey=1.5,
          xanchor="center", 
          yanchor="middle",
          layer="below"
        ),
  dict(
          source="https://1vs1-7f65.kxcdn.com/img/players/players/cristiano-ronaldo-dos-santos-aveiro_834_52-ub-800-mobile.png",
          xref="paper", 
          yref="paper",
          x=0.05, 
          y=0.5,
          sizex=1, 
          sizey=1.6,
          xanchor="center", 
          yanchor="middle",
          layer="below"
        )]

  fig.update_layout(
  paper_bgcolor="rgb(241, 229, 172)",
  title=f'<b>                           L. Messi VS Cristiano Ronaldo</b>',
#     shapes=[go.layout.Shape(
#     type='rect',
#     xref='paper',
#     yref='paper',
#     x0=0,
#     y0=0,
#     x1=1.14,
#     y1=1.15,
#     line={'width': 1, 'color': 'black'}
#     )],
  height=600,
  margin=dict(
      l=10,
      r=10,
      b=10,
      t=100,
      pad=4
  ),
  polar=dict(
      bgcolor = "rgb(241, 229, 172)",
      radialaxis=dict(
          visible = True,
          range = [0, 100]
      ),
      angularaxis=dict(
          showline=False,
          showgrid=False,
          tickfont=dict(
              size=9,
          ),
      )
  )

)




  return fig
  
def cleaning(df):
  df = df.drop(columns = ['player_url', 'long_name', 'dob', 'height_cm', 'weight_kg', 'club_team_id', 'league_level', 
                          'club_position', 'club_jersey_number', 'club_loaned_from', 'club_joined',
                          'club_contract_valid_until', 'nationality_id', 'nation_position','nation_jersey_number','real_face', 'release_clause_eur',
                           'player_tags', 'player_traits','pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic',
                           'attacking_crossing', 'attacking_finishing', 'attacking_heading_accuracy', 'attacking_short_passing',
                           'attacking_volleys', 'skill_dribbling', 'skill_curve', 'skill_fk_accuracy', 'skill_long_passing',
                           'skill_ball_control', 'movement_acceleration', 'movement_sprint_speed', 'movement_agility', 'movement_reactions',
                           'movement_balance', 'power_shot_power', 'power_jumping', 'power_stamina', 'power_strength',
                           'power_long_shots', 'mentality_aggression', 'mentality_interceptions', 'mentality_positioning', 'mentality_vision',
                           'mentality_penalties', 'mentality_composure', 'defending_marking_awareness', 'defending_standing_tackle',
                           'defending_sliding_tackle', 'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
                           'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed', 'ls', 'st', 'rs', 'lw',
                           'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram', 'lm', 'lcm', 'cm', 'rcm', 'rm', 'lwb', 'ldm', 'cdm',
                           'rdm', 'rwb', 'lb', 'lcb', 'cb', 'rcb', 'rb', 'gk', 'player_face_url', 'club_logo_url', 'club_flag_url',
                           'nation_logo_url', 'nation_flag_url'])
  for i in range(len(df)):
      df['player_positions'][i] = df['player_positions'][i][0:2]
  return df
  
def positions_league(df):
  df = cleaning(df)
  result = df.groupby(['league_name', 'player_positions']).size().reset_index(name='count')
  leagues = ['Spain Primera Division', 'German 1. Bundesliga', 'French Ligue 1', 'English Premier League', 'Italian Serie A']
  league_graph = result[result['league_name'].isin(leagues)]
  fig = px.line_polar(league_graph, r="count", theta="player_positions", color = 'league_name', line_close=True)
  fig.update_layout(
#         shapes=[go.layout.Shape(
#         type='rect',
#         xref='paper',
#         yref='paper',
#         x0=-0.11,
#         y0=-0.13,
#         x1=1.30,
#         y1=1.15,
#         line={'width': 1, 'color': 'black'}
#         )],
  plot_bgcolor="rgb(241, 229, 172)",
  paper_bgcolor="rgb(241, 229, 172)",
  title=f'<b>             Positions distribution in the top 5 leagues')
  height=600,
  return fig
  
def categorizing(position):
  if position in ['LW', 'RW', 'CF', 'ST']:
      return 'Forward'
  elif position in ['RM', 'CM', 'LM']:
      return 'Midfielder'
  else:
      return 'Defender'
      
def wages_sunburst(df):
  df['position'] = df['player_positions'].apply(categorizing)
  leagues = ['Spain Primera Division', 'German 1. Bundesliga', 'French Ligue 1', 'English Premier League', 'Italian Serie A']
  df = df[df['league_name'].isin(leagues)]
  grouped = df.groupby(['position', 'league_name']).mean()
  grouped = grouped.rename(columns={'value_eur': 'avg_value'})
  gr = pd.DataFrame(grouped['wage_eur']).reset_index()
  fig = px.sunburst(gr, path=['position', 'league_name'], values='wage_eur', color='wage_eur')
  fig.update_layout(
#         shapes=[go.layout.Shape(
#         type='rect',
#         xref='paper',
#         yref='paper',
#         x0=0,
#         y0=-0.13,
#         x1=1.13,
#         y1=1.15,
#         line={'width': 1, 'color': 'black'}
#         )],
  paper_bgcolor="rgb(241, 229, 172)",
  title=f'<b>             Wage distribution in the top 5 leagues')
  return fig
  

# import dash
# dash.register_page(__name__)

app = dash.Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])

server = app.server

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
