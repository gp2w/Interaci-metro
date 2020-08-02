import tweepy
import logging
# from prettytable import PrettyTable

logging.basicConfig(format='[%(levelname)s][%(asctime)s]: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)


def get_tweets(api, username):
    logging.info(f'Buscando tweets de {username}')
    logging.info('Extração iniciada')
    tweets = api.user_timeline(
        screen_name=username, tweet_mode="extended", count=200)
    tweets_data = [tweet._json for tweet in tweets]
    logging.info(f'{len(tweets)} tweets extraidos')
    tweets_collection = tweets_data.copy()

    while(len(tweets) != 0):
        try:
            tweets = api.user_timeline(screen_name=username,
                                       tweet_mode="extended",
                                       count=200,
                                       max_id=tweets[len(tweets)-1]._json['id']-1)
            if (len(tweets) == 0):
                logging.info('A extração atingiu seu limite.')
                logging.info(
                    f'Total de tweets extraídos: {len(tweets_collection)}')
                break
            else:
                tweets_data = [tweet._json for tweet in tweets]
                tweets_collection = tweets_collection + tweets_data
                logging.info(f'{len(tweets)} tweets extraidos')

        except tweepy.RateLimitError:
            logging.info('Rate Limit atingido')
            logging.info('Extração de tweets finalizada')
            break

    logging.info('Extração de tweets finalizada')
    return tweets_collection


def get_likes(api, username):
    logging.info(f'Buscando curtidas de: {username}')
    logging.info('Extração iniciada')
    likes = api.favorites(screen_name=username,
                          count=200, tweet_mode="extended")
    logging.info(f'Extraindo {len(likes)} curtidas')
    likes_data = [tweet._json for tweet in likes]
    likes_collection = likes_data.copy()

    while(len(likes) != 0):
        try:
            likes = api.favorites(screen_name=username,
                                  count=200,
                                  tweet_mode="extended",
                                  max_id=likes[len(likes)-1]._json['id']-1)

            if(len(likes) == 0):
                logging.info('A extração atingiu seu limite.')
                logging.info(
                    f'Total de curtidas extraídas: {len(likes_collection)}')
                break
            else:
                likes_data = [tweet._json for tweet in likes]
                likes_collection = likes_collection + likes_data
                logging.info(
                    f'Extraindo {len(likes_data)} curtidas')

        except tweepy.RateLimitError:
            logging.info('Rate Limit atingido')
            break

    logging.info('Extração de curtidas finalizada')
    return likes_collection
