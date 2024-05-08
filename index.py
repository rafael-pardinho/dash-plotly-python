from dash import html, dcc, Input, Output
from dash_bootstrap_templates import ThemeSwitchAIO
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from app import *

# Styles
url_theme1 = dbc.themes.VAPOR
url_theme2 = dbc.themes.FLATLY
template_theme1 = 'vapor'
template_theme2 = 'flatly'

# Reading data
df = pd.read_csv('data_clean.csv')

# State options
state_options = [{'label': x, 'value': x} for x in df['ESTADO'].unique()]

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            ThemeSwitchAIO(aio_id='theme', themes=[url_theme1, url_theme2]),
            html.H3('Preço x Estado'),
            dcc.Dropdown(
                id='estados',
                value=[state['label'] for state in state_options[:3]],
                multi=True,
                options=state_options
            ),
            dcc.Graph(id='line_graph')
        ])
    ])
])

# Rodar o server
if __name__ == '__main__':
    app.run_server(debug=True, port='8051' )