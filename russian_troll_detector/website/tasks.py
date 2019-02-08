import twitter
import json
api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

def get_tweets(username):
    user = api.GetUser(None, username, True, True)
    print(user)
    return user


def calculate_features():
    return None


def make_predictions():
    return None