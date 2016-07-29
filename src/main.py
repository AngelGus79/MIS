from twython import Twython
from user import User
from tweetNavigator import TweetNavigator
from statistics import Statistics
import settings

#Mostrar comentarios por Usuario
tweet_Sayulita = TweetNavigator("#sayulita")
users_Sayulita = tweet_Sayulita.getUsers()
print "\n"   
print "--------------------------------------------------------COMENTARIOS POR USUARIO---------------------------------------------------"   
print "\n"  
u=0
for user in users_Sayulita:
    u += 1
    UserSentiment = users_Sayulita[user].getSentiment()
    print str(u).zfill(2) + ". User name: " + users_Sayulita[user].name + " Gender: " + users_Sayulita[user].gender + "   User Sentiment: " + UserSentiment

    c = 0
    for comment in users_Sayulita[user].comments:
        c += 1
        print "comment " + str(c).zfill(2) + ": " + comment['text']
        print "sentiment: " + comment['sentiment'] + " \n"

    print "-----------------------------------------------------------------------------------------------------------------------------------------------------------------"   
    print "\n"

  
print "-----------------------------------------------------------------------------ESTADISTICAS----------------------------------------------------------------------------"   
print "\n" 

statistics_Sayulita = Statistics(users_Sayulita)
statistics_Sentiment_Sayulita = statistics_Sayulita.getUsersSentiment()

print "female positive: " + str(statistics_Sentiment_Sayulita['female']['positive']) +  "\n"
print "female negative: " + str(statistics_Sentiment_Sayulita['female']['negative']) +  "\n"
print "female neutral: " + str(statistics_Sentiment_Sayulita['female']['neutral']) +  "\n\n"

print "male positive: " + str(statistics_Sentiment_Sayulita['male']['positive']) +  "\n"
print "male negative: " + str(statistics_Sentiment_Sayulita['male']['negative']) +  "\n"
print "male neutral: " + str(statistics_Sentiment_Sayulita['male']['neutral']) +  "\n\n"

print "undefined positive: " + str(statistics_Sentiment_Sayulita['undefined']['positive']) +  "\n"
print "undefined negative: " + str(statistics_Sentiment_Sayulita['undefined']['negative']) +  "\n"
print "undefined neutral: " + str(statistics_Sentiment_Sayulita['undefined']['neutral']) +  "\n\n"

print "all positive: " + str(statistics_Sentiment_Sayulita['all']['positive']) +  "\n"
print "all negative: " + str(statistics_Sentiment_Sayulita['all']['negative']) +  "\n"
print "all neutral: " + str(statistics_Sentiment_Sayulita['all']['neutral']) +  "\n\n"

print "male count: " + str(statistics_Sentiment_Sayulita['male']['count']) +  "\n"
print "female count: " + str(statistics_Sentiment_Sayulita['female']['count']) +  "\n"
print "undefined count: " + str(statistics_Sentiment_Sayulita['undefined']['count']) +  "\n"
print "all count: " + str(statistics_Sentiment_Sayulita['all']['count']) +  "\n"







