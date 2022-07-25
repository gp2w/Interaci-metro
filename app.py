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

app.layout = dbc.Container([
    navbar,
    html.Br(),
    html.Div(id="the-alert", children=[]),
    html.Br(),
    dbc.Row(
        dbc.Col(
            dbc.Form(
                dbc.FormGroup([
                    dbc.Label("Digite um usuário do twitter para realizar uma busca", html_for="user-input"),
                    dbc.InputGroup(
                        [
                            dbc.InputGroupAddon("@", addon_type="prepend"),
                            dbc.Input(id="user-input", value="", type="text", n_submit=0),
                            dbc.InputGroupAddon(
                                dbc.Button("Buscar", id="submit-button", type="submit", n_clicks=0),
                                addon_type="append",
                            ),
                        ]
                    )
                ]),
            ),
            xs=12,
            md={"size": 6, "offset": 3},
            lg={"size": 4, "offset": 4}
        ),
        form=True
    ),
    html.Br(),
    dcc.Loading(
        id="loading",
        type="graph",
        children=[
            dbc.Row(dbc.Col(
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
                    page_size=15,
                    style_as_list_view=True,
                    style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                    style_cell={
                        'backgroundColor': 'rgb(50, 50, 50)',
                        'color': 'white'
                    },
                ),
                width={"size": 10, "offset": 1}
            )),
            html.Div([], style={'margin': 50}),
            dbc.Row(dbc.Col(
                html.Div(id='datatable-row-ids-container'),
                width={"size": 10, "offset": 1}
            )),
        ]
    )
    
],
id="index",
style={"padding-right": 0,"padding-left":0, "overflow": "hidden"},
fluid=True)

from callbacks import *

if __name__ == '__main__':
    app.run_server(debug=True)
