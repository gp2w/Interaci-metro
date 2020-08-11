import numpy as np
import pandas as pd
from datetime import datetime, timedelta

logging.basicConfig(format='[%(levelname)s][%(asctime)s]: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)

def top_users_likes(likes):
    screen_names = np.array([like['user']['screen_name'] for like in likes])
    user, count = np.unique(screen_names, return_counts=True)
    df = pd.DataFrame({'user': user, 'num_likes': count})
    df = df.sort_values(by=['num_likes'], ascending=False)
    df = df.reset_index()
    df.drop(columns=['index'], inplace=True)

    return df

def top_users_replies(tweets):
    screen_names = np.array([tweet['in_reply_to_screen_name']
                             for tweet in tweets if tweet['in_reply_to_screen_name'] is not None])
    user, count = np.unique(screen_names, return_counts=True)
    df = pd.DataFrame({'user': user, 'num_replies': count})
    df = df.sort_values(by=['num_replies'], ascending=False)
    df = df.reset_index()
    df.drop(columns=['index'], inplace=True)

    return df

def top_users_retweets(tweets):
    screen_names = np.array([tweet['retweeted_status']['user']['screen_name']
                             for tweet in tweets if "retweeted_status" in tweet])
    user, count = np.unique(screen_names, return_counts=True)
    df = pd.DataFrame({'user': user, 'num_retweets': count})
    df = df.sort_values(by=['num_retweets'], ascending=False)
    df = df.reset_index()
    df.drop(columns=['index'], inplace=True)
    
    return df

def score(likes_df, replies_df, retweets_df):
    df = likes_df.join(replies_df.set_index('user'), on='user').join(
        retweets_df.set_index('user'), on='user')
    df.fillna(0, inplace=True)
    df[['num_replies', 'num_retweets']] = df[[
        'num_replies', 'num_retweets']].astype(dtype='int32')
    df['score'] = df['num_likes']*1.0 + \
        df['num_replies']*1.1 + df['num_retweets']*1.3
    df = df.sort_values(by=['score'], ascending=False).reset_index(drop=True)
    df['score'] = df['score'].map('{:,.1f}'.format)

    return df

def tweets_per_hour(tweets):
    hours = np.array(
        [(datetime.strptime(tweet['created_at'],
                            '%a %b %d %H:%M:%S %z %Y') - timedelta(hours=3)).time().hour for tweet in tweets]
    )
    hour, count = np.unique(hours, return_counts=True)
    df = pd.DataFrame({'hour': hour, 'count': count})
    df = df.sort_values(by=['hour'], ascending=True)
    df = df.reset_index()
    df.drop(columns=['index'], inplace=True)

    return df
