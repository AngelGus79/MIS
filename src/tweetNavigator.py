# -*- coding: utf-8 -*-
from twython import Twython
from user import User
import settings


class tweetNavigator:
    def __init__(self, hashtag):
        self.hashtag = hashtag

        self.twython = Twython(
            app_key=settings.TWITTER_APP_KEY,
            app_secret=settings.TWITTER_APP_KEY_SECRET,
            oauth_token=settings.TWITTER_ACCESS_TOKEN,
            oauth_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)

    def getUsers(self):
        search = self.twython.search(q=self.hashtag)

        tweets = search['statuses']
        users_dictionary = {}

        for tweet in tweets:
            u = User()

            if not users_dictionary.has_key(tweet['id_str']):
                u.name = tweet["user"]["name"].encode("utf-8")
                u.comments.append(tweet['text'])
                users_dictionary[tweet['id_str']] = u
            else:
                u = users_dictionary[tweet['id_str']]
                u.comments.append(tweet['text'])
                users_dictionary[tweet['id_str']] = u

        return users_dictionary

    def getComments(self):
        print "algo"
