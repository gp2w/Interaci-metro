import tweepy
import json
import argparse
from core.utils import to_json
from core.coletar_dados import get_tweets, get_likes
from core.processar_dados import top_users_likes, top_users_replies


def main():
    
    parser = argparse.ArgumentParser(prog='get_tweets.py')

    parser.add_argument(
        '--username', type=str, help='Username do perfil, acompanhado do @', required=True)

    parser.add_argument(
        '--output', type=str, help='Nome do arquivo contendo os tweets')

    args = parser.parse_args()

    with open('tokens.json', 'r') as file:
        tokens = json.load(file)

    auth = tweepy.OAuthHandler(tokens['api_key'], tokens['api_secret_key'])
    auth.set_access_token(tokens['access_token'],
                          tokens['access_token_secret'])
    api = tweepy.API(auth)

    tweets = get_tweets(api=api, username=args.username)
    likes = get_likes(api=api, username=args.username)

    if(args.output):
        to_json(obj=tweets, filename=args.output)
        to_json(obj=likes, filename=args.output)
    else:
        to_json(obj=tweets, filename=args.username+'_tweets')
        to_json(obj=likes, filename=args.username+'_likes')

    print(top_users_likes(likes=likes))
    print(top_users_replies(tweets=tweets))


if __name__ == "__main__":
    main()
