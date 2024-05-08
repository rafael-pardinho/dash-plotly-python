from dash import html, dcc, Input, Output
from dash_bootstrap_templates import ThemeSwitchAIO
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from app import *

# Reading data
df = pd.read_csv('data_clean.csv')

# Layout
app.layout = dbc.Container([
    html.H1('TESTE')
])

# Rodar o server
if __name__ == '__main__':
    app.run_server(debug=True, port='8051' )