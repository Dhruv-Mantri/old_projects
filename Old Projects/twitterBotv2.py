import tweepy

api_key = "[insert API key]"
api_key_secret = "[insert secret API key]"
access_token = "[insert access token]"
access_token_secret = "[insert secret access token]"

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.Client(consumer_key= api_key,consumer_secret= api_key_secret,access_token= access_token,access_token_secret= access_token_secret)

creator = api.get_user(username= "[your username]")
# api.follow()
print(creator.name)
