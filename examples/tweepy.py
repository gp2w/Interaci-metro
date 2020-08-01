import tweepy
import json

access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
api_key = "your_api_key"
api_secret_key = "your_api_secret_key"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# busca geral
dados0 = api.search(q='space', count=13)
tweets0 = [d._json for d in dados0]

# buscar tweets de um @
dados1 = api.user_timeline(screen_name='Twitter', count=13)
tweets1 = [d._json for d in dados1]

# print
# print(json.dumps(tweets0[0], indent=3, ensure_ascii=False))
print(json.dumps(tweets1[0], indent=3, ensure_ascii=False))