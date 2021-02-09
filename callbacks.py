import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import pandas as pd
import logging

from app import app, df, alert
from api import api
from core import coletar_dados as core_cd, processar_dados as core_pd

@app.callback(
    [Output('the-alert', 'children'), Output('datatable-row-ids', 'data')],
    [Input('submit-button', 'n_clicks'), Input('user-input', 'n_submit')],
    [State('user-input', 'value')])
def update_username(n_clicks, n_submit, username):

    # reseta dataframe
    df = pd.DataFrame(columns=['user', 'num_likes'])
    retornos = [dash.no_update, dash.no_update]

    if username != '':

        tweets = core_cd.get_tweets(api=api, username=username)

        if(tweets is not None):
            likes = core_cd.get_likes(api=api, username=username)

            likes_df = core_pd.top_users_likes(likes=likes)

            replies_df = core_pd.top_users_replies(tweets=tweets)
            # tratamento para retirar o próprio usuário das replies
            index = replies_df['user'] == username
            replies_df = replies_df.drop(replies_df.index[index])

            retweets_df = core_pd.top_users_retweets(tweets=tweets)

            df = core_pd.score(likes_df, replies_df, retweets_df)

            # filtrar scores maiores que 10
            index = pd.to_numeric(df['score']) > 10.0
            df = df[index]

            retornos = [dash.no_update, df.to_dict('records')]
        else:
            logging.info(f'Token Inválido ou Expirado.')
            retornos = [alert, dash.no_update]

    return retornos

@app.callback(
    Output('datatable-row-ids-container', 'children'),
    [Input('datatable-row-ids', 'derived_virtual_data')])
def update_graphs(rows):

    dff = pd.DataFrame(data=rows, columns=['user', 'num_likes', 'num_replies', 'num_retweets', 'score'])

    return [
        # gráfico com likes, replies e retweets
        dcc.Graph(
            id='interações',
            figure={
                'data': [
                    {
                        'x': dff['user'],
                        'y': dff['num_likes'],
                        'type': 'bar',
                        'name': 'Likes'
                    },
                    {
                        'x': dff['user'],
                        'y': dff['num_replies'],
                        'type': 'bar',
                        'name': 'Replies'
                    },
                    {
                        'x': dff['user'],
                        'y': dff['num_retweets'],
                        'type': 'bar',
                        'name': 'Retweets'
                    }
                ],
                'layout': {
                    'xaxis': {
                        'automargin': True,
                    },
                    'yaxis': {
                        'automargin': True,
                        'title': {'text': 'interações'}
                    },
                    'height': 250,
                    'margin': {'t': 10, 'l': 10, 'r': 10}
                },
            },
        ),
        # gráfico com o score de interação
        dcc.Graph(
            id='score',
            figure={
                'data': [
                    {
                        'x': dff['user'],
                        'y': dff['score'],
                        'type': 'bar'
                    }
                ],
                'layout': {
                    'xaxis': {
                        'automargin': True,
                    },
                    'yaxis': {
                        'automargin': True,
                        'title': {'text': 'score'}
                    },
                    'height': 250,
                    'margin': {'t': 10, 'l': 10, 'r': 10}
                },
            },
        )
        # for column in ['num_likes', 'num_replies', 'num_retweets', 'score'] if column in dff
    ]

# add callback for toggling the collapse on small screens
""" 
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
"""