# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
import tweepy

import core.coletar_dados as core_cd
import core.processar_dados as core_pd

# importar css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# carregar variaveis de ambiente do .env caso exista
from dotenv import load_dotenv
load_dotenv()

# inicializa api do twitter
auth = tweepy.OAuthHandler(os.environ['API_KEY'], os.environ['API_SECRET_KEY'])
auth.set_access_token(os.environ['ACCESS_TOKEN'],
                      os.environ['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)

# tweets = core_cd.get_tweets(api=api, username='weversonvn')
# likes = core_cd.get_likes(api=api, username='weversonvn')
# inicializa dataframe vazio
df = core_pd.top_users_likes(likes=[])

df['id'] = df['user']
df.set_index('id', inplace=True, drop=False)

# inicializa uma aplicacao em Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server # the Flask app

app.layout = html.Div([
    html.H2("Interaciômetro"),
    html.H5("Digite um usuario do twitter para realizar uma busca"),
    html.Div([
        "Usuario: ", 
        dcc.Input(id='user-input', value='', type='text'),
        html.Button(id='submit-button-state', n_clicks=0, children='Buscar'),
    ]),
    html.Br(),
    dash_table.DataTable(
        id='datatable-row-ids',
        columns=[
            {'name': i, 'id': i, 'deletable': False} for i in df.columns
            # omit the id and index column
            if i != 'id' and i != 'index'            
        ],
        data=df.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode='multi',
        row_selectable='multi',
        row_deletable=False,
        selected_rows=[],
        page_action='native',
        page_current= 0,
        page_size= 10,
    ),
    html.Div(id='datatable-row-ids-container')
])

@app.callback(Output('datatable-row-ids', 'data'),
              [Input('submit-button-state', 'n_clicks')],
              [State('user-input', 'value')])
def update_username(n_clicks, username):
    # apaga dataframe anterior
    df = core_pd.top_users_likes(likes=[])
    if username != '':

        # tweets = core_cd.get_tweets(api=api, username='weversonvn')
        likes = core_cd.get_likes(api=api, username=username)

        df = core_pd.top_users_likes(likes=likes)

        df['id'] = df['user']
        df.set_index('id', inplace=True, drop=False)

    return df.to_dict('records')

@app.callback(
    Output('datatable-row-ids-container', 'children'),
    [Input('datatable-row-ids', 'derived_virtual_row_ids'),
     Input('datatable-row-ids', 'selected_row_ids'),
     Input('datatable-row-ids', 'active_cell')])
def update_graphs(row_ids, selected_row_ids, active_cell):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncracy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    selected_id_set = set(selected_row_ids or [])

    if row_ids is None:
        dff = df
        # pandas Series works enough like a list for this to be OK
        row_ids = df['id']
    else:
        dff = df.loc[row_ids]

    active_row_id = active_cell['row_id'] if active_cell else None

    colors = ['#FF69B4' if id == active_row_id
              else '#7FDBFF' if id in selected_id_set
              else '#0074D9'
              for id in row_ids]

    return [
        dcc.Graph(
            id=column + '--row-ids',
            figure={
                'data': [
                    {
                        'x': dff['user'],
                        'y': dff[column],
                        'type': 'bar',
                        'marker': {'color': colors},
                    }
                ],
                'layout': {
                    'xaxis': {'automargin': True},
                    'yaxis': {
                        'automargin': True,
                        'title': {'text': column}
                    },
                    'height': 250,
                    'margin': {'t': 10, 'l': 10, 'r': 10},
                },
            },
        )
        # check if column exists - user may have deleted it
        # If `column.deletable=False`, then you don't
        # need to do this check.
        for column in ['count'] if column in dff
    ]

if __name__ == '__main__':
    app.run_server(debug=True)