import unittest
import os
import sys

# Update python path
test_path = os.path.abspath(os.path.join(__file__, os.pardir))
project_path = os.path.abspath(os.path.join(test_path, os.pardir))
sys.path.append(project_path)

from src.user import User
from src.statistics import Statistics


class TweetNavigatorTest(unittest.TestCase):

    def setUp(self):
        juan = User(name='Juan')
        juan.gender = 'male'
        juan.comments = [
            {'text': 'Hola mundo', 'sentiment': 'pos'},
        ]

        fatima = User(name='Fatima')
        fatima.gender = 'female'
        fatima.comments = [
            {'text': 'Hola mundo', 'sentiment': 'pos'},
        ]

        pedro = User(name='Pedro')
        pedro.gender = 'male'
        pedro.comments = [
            {'text': 'Hola mundo', 'sentiment': 'neg'},
        ]

        self.users = {
            '1234': juan,
            '1010': fatima,
            '2222': pedro,
        }

    def test_getUsersCount(self):
        s = Statistics(self.users)
        counts = s.getUsersCount()
        self.assertEqual(2, counts['male'])
        self.assertEqual(1, counts['female'])
        self.assertEqual(0, counts['undefined'])
        self.assertEqual(3, counts['total'])

    def test_getUsersSentiment(self):
        s = Statistics(self.users)
        sentiments = s.getUsersSentiment()

        # Conteo de sentimientos solo female
        self.assertEqual(1, sentiments['female']['positive'])
        self.assertEqual(0, sentiments['female']['negative'])
        self.assertEqual(0, sentiments['female']['neutral'])
        self.assertEqual(1, sentiments['female']['count'])

        # Conteo de sentimientos solo male
        self.assertEqual(1, sentiments['male']['positive'])
        self.assertEqual(1, sentiments['male']['negative'])
        self.assertEqual(0, sentiments['male']['neutral'])
        self.assertEqual(2, sentiments['male']['count'])

        # Conteo de sentimientos solo indefinidos
        self.assertEqual(0, sentiments['undefined']['positive'])
        self.assertEqual(0, sentiments['undefined']['negative'])
        self.assertEqual(0, sentiments['undefined']['neutral'])
        self.assertEqual(0, sentiments['undefined']['count'])

        # Conteo de sentimientos por todos los usuarios
        self.assertEqual(2, sentiments['all']['positive'])
        self.assertEqual(1, sentiments['all']['negative'])
        self.assertEqual(0, sentiments['all']['neutral'])
        self.assertEqual(3, sentiments['all']['count'])

if __name__ == '__main__':
    unittest.main()
