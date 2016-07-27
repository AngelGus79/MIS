from twython import Twython
import settings

class tweetNavigator:
    def __init__(self, hashtag):
        self.hashtag = hashtag

    def getUsers(self):
        t = Twython(app_key=settings.TWITTER_APP_KEY,
        app_secret=settings.TWITTER_APP_KEY_SECRET,
        oauth_token=settings.TWITTER_ACCESS_TOKEN,
        oauth_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)

        search = t.search(q=self.hashtag)

        tweets = search['statuses']
        lista_de_Usuarios = []
        for tweet in tweets:
            lista_de_Usuarios.append(tweet["user"]["name"].encode("utf-8"))


        return list(set(lista_de_Usuarios))
    
    def getComments(self):
        print "algo"



