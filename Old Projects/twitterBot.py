import tweepy
import time

api_key = "4lmp6WTg3SHWI7d6KPTAHFJyT"
api_key_secret = "cSFNdipcDUlKhue3ZkIeLxVDUhMrb5MWpbEihXSBorKG9x6MaN"
access_token = "1449900639689998336-Uzeho8Wd89KLXge3cCXE7yMuPL26fB"
access_token_secret = "gmMyOSCWXPXHGZrv352FjGR6ecLOOFsHKYPDXB8K0e2yA"

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

creator = api.get_user(screen_name= "PineappleLord47")


# api.create_friendship(screen_name=creator)

# tweets = tweepy.Cursor(api.search, q="who", lang="en").items(10)
#
# for tweet in tweets:
#     print(tweet.text)



def get_tweets(keyword, num):

    fetched = api.search_tweets(q=keyword,count= num)

    # print(fetched)
    for tweet in fetched:
        twt = str(tweet.text).split(" ")
        if twt[0] == "RT":
            if str(twt[2]).lower() == keyword.lower():
                if not tweet.favorited:
                    try:
                        # if str(tweet.author.screen_name) == "MasterDhruv1":
                        #     api.update_status("The Future", tweet.id)
                        api.update_status(status="your mom", in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
                        api.create_favorite(tweet.id)
                        print(tweet.text)
                    except:
                        continue

while True:
    get_tweets("What", 1000)
    get_tweets("Who", 1000)
    time.sleep(3600)