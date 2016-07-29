# -*- coding: utf-8 -*-
from twython import Twython
from user import User
import settings
import requests


class TweetNavigator:
    def __init__(self, hashtag):
        self.hashtag = hashtag

        self.twython = Twython(
            app_key=settings.TWITTER_APP_KEY,
            app_secret=settings.TWITTER_APP_KEY_SECRET,
            oauth_token=settings.TWITTER_ACCESS_TOKEN,
            oauth_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)

    def getSentiment(self, text):
        endpoint = 'https://japerk-text-processing.p.mashape.com/sentiment/'
        headers = {
            'X-Mashape-Key': settings.MASHAPE_KEY,
        }

        payload = {
            'language': 'english',
            'text': text,
        }

        response = requests.post(endpoint, headers=headers, data=payload)
        # {"probability": {"neg": 0.36525227438916918, "neutral": 0.56068716327814216, "pos": 0.63474772561083082}, "label": "neutral"}
        response = response.json()

        return {
            'text': text,
            'sentiment': response['label'],
        }

    def getUsers(self):
        search = self.twython.search(q=self.hashtag)

        tweets = search['statuses']
        users_dictionary = {}
        users_list = []

        for tweet in tweets:
            u = User()

            if not users_dictionary.has_key(tweet['user']['id']):
                u.name = tweet["user"]["name"].encode("utf-8")

                comment = self.getSentiment(tweet['text'].encode('utf-8'))
                u.comments.append(comment)

                users_dictionary[tweet['user']['id']] = u
                users_list.append(u.getFormatedName())
            else:
                u = users_dictionary[tweet['user']['id']]

                comment = self.getSentiment(tweet['text'].encode('utf-8'))
                u.comments.append(comment)

                users_dictionary[tweet['user']['id']] = u

        #Asignacion de genero
        payload = {'name[]': users_list}
        response = requests.get('https://api.genderize.io', params=payload)
        genders_dictionary = response.json()
        
        for user in users_dictionary:
            for gender in genders_dictionary:
                if users_dictionary[user].formated_name == gender["name"].encode('utf-8'):
                    if not gender["gender"]:
                        users_dictionary[user].gender = 'undefined'
                    else:
                        users_dictionary[user].gender = gender["gender"].encode('utf-8')

                    genders_dictionary.remove(gender)
                    break
      
        return users_dictionary


         

 

