# -*- coding: utf-8 -*-
from twython import Twython
import settings

# Ejemplo de tweets
t = Twython(app_key=settings.TWITTER_APP_KEY,
            app_secret=settings.TWITTER_APP_KEY_SECRET,
            oauth_token=settings.TWITTER_ACCESS_TOKEN,
            oauth_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#sayulita')

tweets = search['statuses']

for tweet in tweets:
    print tweet

# Ejemplo de genero
import requests
names = ['John', 'Lauren', 'Peter']

payload = {'name[]': names}
response = requests.get('https://api.genderize.io', params=payload)
print response.json()

# Ejemplo de análisis de sentimiento
import requests

endpoint = 'https://japerk-text-processing.p.mashape.com/sentiment/'
headers = {
    'X-Mashape-Key': settings.MASHAPE_KEY,
}

payload = {
    'language': 'english',
    'text': 'see you later',
}

response = requests.post(endpoint, headers=headers, data=payload)
print response.text
# {"probability": {"neg": 0.36525227438916918, "neutral": 0.56068716327814216, "pos": 0.63474772561083082}, "label": "neutral"}
