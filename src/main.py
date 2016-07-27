# -*- coding: utf-8 -*-
from twython import Twython
import settings

t = Twython(app_key=settings.TWITTER_APP_KEY,
            app_secret=settings.TWITTER_APP_KEY_SECRET,
            oauth_token=settings.TWITTER_ACCESS_TOKEN,
            oauth_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#sayulita')

tweets = search['statuses']

for tweet in tweets:
    print tweet
   
