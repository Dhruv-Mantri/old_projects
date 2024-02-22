import tweepy
import time

api_key = "[api key]"
api_key_secret = "[secret api key]"
access_token = "[access token]"
access_token_secret = "[secret access token]"

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

creator = api.get_user(screen_name= "[your username]")


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
                        # if str(tweet.author.screen_name) == "[]":
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
