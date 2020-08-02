import logging
import numpy as np
import pandas as pd
from prettytable import PrettyTable

logging.basicConfig(format='[%(levelname)s][%(asctime)s]: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)

def top_users_likes(likes, num_users=20):
    logging.info(f'Computando os {num_users} usuários mais curtidos')
    screen_names = np.array([like['user']['screen_name'] for like in likes])
    user, count = np.unique(screen_names, return_counts=True)
    df = pd.DataFrame({'user': user, 'count': count})
    df = df.sort_values(by=['count'], ascending=False)
    df = df.reset_index()

    table = PrettyTable()
    table.field_names = ["position", "user", "likes"]
    for i, j in enumerate(df.index):
        table.add_row([i+1, df['user'][j], df['count'][j]])

    with open(f'ranking_likes.txt', 'w') as w:
        w.write(str(table))

    return table.get_string(start=0, end=num_users)


def top_users_replies(tweets, num_users=20):
    logging.info(f'Computando os {num_users} usuários mais respondidos')
    screen_names = np.array([tweet['in_reply_to_screen_name']
                             for tweet in tweets if tweet['in_reply_to_screen_name'] is not None])
    user, count = np.unique(screen_names, return_counts=True)
    df = pd.DataFrame({'user': user, 'count': count})
    df = df.sort_values(by=['count'], ascending=False)
    df = df.reset_index()

    table = PrettyTable()
    table.field_names = ["position", "user", "replies"]
    for i, j in enumerate(df.index):
        table.add_row([i+1, df['user'][j], df['count'][j]])

    with open(f'ranking_replies.txt', 'w') as w:
        w.write(str(table))

    return table.get_string(start=0, end=num_users)