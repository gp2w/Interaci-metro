from os import environ
from tweepy import OAuthHandler, API
from dotenv import load_dotenv

# carregar variaveis de ambiente do .env caso exista
load_dotenv()

# inicializa api do twitter
auth = OAuthHandler(environ['API_KEY'], environ['API_SECRET_KEY'])
auth.set_access_token(environ['ACCESS_TOKEN'], environ['ACCESS_TOKEN_SECRET'])
api = API(auth)