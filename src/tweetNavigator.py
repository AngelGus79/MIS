# -*- coding: utf-8 -*-
from twython import Twython
from user import User
import settings
import requests


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
        users_list = []
        

        for tweet in tweets:
            u = User()

            if not users_dictionary.has_key(tweet['user']['id']):
                u.name = tweet["user"]["name"].encode("utf-8")
                u.comments.append(tweet['text'].encode("utf-8"))
                users_dictionary[tweet['user']['id']] = u
                users_list.append(u.getFormatedName())
            else:
                u = users_dictionary[tweet['user']['id']]
                u.comments.append(tweet['text'].encode("utf-8"))
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
                        users_dictionary[user].gender = gender["gender"]

                    genders_dictionary.remove(gender)
                    break
      
        return users_dictionary

    def getComments(self):
        print "algo"

tn = tweetNavigator("#sayulita")
usuarios = tn.getUsers()

for u in usuarios:
    print "Usuario: " + usuarios[u].formated_name + " Genero: " + usuarios[u].gender
    for c in usuarios[u].comments:
        print "comentario: " + c
