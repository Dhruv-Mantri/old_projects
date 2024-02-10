import tweepy

api_key = "4lmp6WTg3SHWI7d6KPTAHFJyT"
api_key_secret = "cSFNdipcDUlKhue3ZkIeLxVDUhMrb5MWpbEihXSBorKG9x6MaN"
access_token = "1449900639689998336-Uzeho8Wd89KLXge3cCXE7yMuPL26fB"
access_token_secret = "gmMyOSCWXPXHGZrv352FjGR6ecLOOFsHKYPDXB8K0e2yA"

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.Client(consumer_key= api_key,consumer_secret= api_key_secret,access_token= access_token,access_token_secret= access_token_secret)

creator = api.get_user(username= "MasterDhruv1")
# api.follow()
print(creator.name)