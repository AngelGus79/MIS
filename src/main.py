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
