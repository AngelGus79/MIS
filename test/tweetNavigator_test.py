import mock
import unittest
import os
import sys
import httpretty

# Update python path
test_path = os.path.abspath(os.path.join(__file__, os.pardir))
project_path = os.path.abspath(os.path.join(test_path, os.pardir))
sys.path.append(project_path)

from src.tweetNavigator import tweetNavigator, User


class TweetNavigatorTest(unittest.TestCase):

    @httpretty.activate
    # @mock.patch('src.tweetNavigator.tweetNavigator.getSentiment')
    @mock.patch('src.tweetNavigator.Twython')
    def test_getUsers(self, mock_tw):
        mock_tw().search.return_value = {
            'statuses': [
                {
                    'user': {'name': 'Juan', 'id': '1122'},
                    'text': 'Hola'
                },
                {
                    'user': {'name': 'Pedro', 'id': '1234'},
                    'text': 'Adios',
                },
            ]
        }

        httpretty.register_uri(
            httpretty.POST,
            'https://japerk-text-processing.p.mashape.com/sentiment/',
            body='''
            {
              "probability": {
                "neg": 0.36525227438916918,
                "neutral": 0.56068716327814216,
                "pos": 0.63474772561083082
               },
              "label": "neutral"
            }
            ''',
            content_type="application/json")

        httpretty.register_uri(
            httpretty.GET,
            'https://api.genderize.io/?name[0]=Juan&name[1]=Pedro',
            body='''
            [
                {"name":"Juan","gender":"male","probability":"1.00","count":796},
                {"name":"Pedro","gender":"female","probability":"0.94","count":70}
            ]
            ''',
            content_type="application/json")

        navigator = tweetNavigator('sayulita')
        users = navigator.getUsers()

        self.assertEqual(2, len(users))
        user = users['1122']
        self.assertIsInstance(user, User)
        self.assertEqual('Juan', user.name)
        self.assertEqual('male', user.gender)

        self.assertEqual(
            [{'sentiment': 'neutral', 'text': 'Hola'}],
            user.comments)


if __name__ == '__main__':
    unittest.main()
