#!/usr/bin/env python
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from server import app

import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from layouts.navbar import navbar

# inicializando dataframe
df = pd.DataFrame(columns=['user', 'num_likes', 'num_replies', 'num_retweets', 'score'])

alert = dbc.Alert(["No momento não é possivel realizar novas requisições.", html.Br(), "Por favor, tente mais tarde."],
                color="danger",
                dismissable=True) # use dismissable or duration=5000 for alert to close in x milliseconds

app.layout = html.Div(dbc.Container([
    # navbar,
    html.H2("Interaciômetro"),
    html.H5("Digite um usuário do twitter para realizar uma busca"),
    html.Div([
        "@ ",
        dcc.Input(id='user-input', value='', type='text', n_submit=0),
        html.Button(id='submit-button', type="submit", n_clicks=0, children='Buscar', style={'margin-left': 10}),
    ], style={'padding': 10}),
    html.Br(),
    html.Div(id="the-alert", children=[]),
    html.Br(),
    dcc.Loading(
        id="loading",
        type="graph",
        children=[
            dash_table.DataTable(
                id='datatable-row-ids',
                columns=[
                    {'name': 'Usuário', 'id': 'user'},
                    {'name': 'Likes', 'id': 'num_likes'},
                    {'name': 'Replies', 'id': 'num_replies'},
                    {'name': 'Retweets', 'id': 'num_retweets'},
                    {'name': 'Score', 'id': 'score'}
                ],
                data=df.to_dict('records'),
                filter_action="native",
                sort_action="native",
                sort_mode='multi',
                page_action='native',
                page_current=0,
                page_size=15
            ),
            html.Div([], style={'margin': 50}),
            html.Div(id='datatable-row-ids-container')
        ]
    )
],
# className="p-3"
))

from callbacks import *

if __name__ == '__main__':
    app.run_server(debug=True)
