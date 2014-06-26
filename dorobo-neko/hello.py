import tweepy

consumer_key = "kTHP8XDGBKkhbGFLVEYHJmLE6"
consumer_secret = "8uVyZg7MCIjmrT1zbzOMXUy2GmpErR5FvjN2BZ55Dj2N34rp5F"
access_token = "2589034873-iUqQ6j4UdUzdem3BJSNTAhDvOJSGCjUw0gTDAb5"
access_token_secret = "LQAurpOmDZFxk2cH8kZLXYqyEIFW7XvkE8XVaJdCMJf5c"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
