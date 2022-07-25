import dash
import dash_bootstrap_components as dbc
from constants.metatags import metatags

# inicializa uma aplicacao em Dash
app = dash.Dash(__name__, title='Interaciômetro | GP2W', external_stylesheets=[dbc.themes.DARKLY], meta_tags=metatags)

# expoem variavel server para o Procfile
server = app.server