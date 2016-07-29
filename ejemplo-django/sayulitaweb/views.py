from django.views.generic import TemplateView
from MIS.src.tweetNavigator import TweetNavigator
from MIS.src.statistics import Statistics


class SayulitaView(TemplateView):

    template_name = 'sayulita.html'

    def get_context_data(self, **kwargs):
        context = super(SayulitaView, self).get_context_data(**kwargs)

        hashtag = 'sayulita'

        t = TweetNavigator(hashtag)
        s = Statistics(t.getUsers())

        context['data'] = s.getUsersSentiment()
        context['hashtag'] = hashtag

        return context
