import mock
import unittest
import os
import sys
import httpretty

# Update python path
test_path = os.path.abspath(os.path.join(__file__, os.pardir))
project_path = os.path.abspath(os.path.join(test_path, os.pardir))
sys.path.append(project_path)

from src.user import User


class TestUser(unittest.TestCase):

    def test_getSentiment(self):
        u = User(name='John Doe')
        u.comments = [
            {'text': 'Hola mundo', 'sentiment': 'pos'},
            {'text': 'Hello world', 'sentiment': 'pos'},
            {'text': 'Bad word', 'sentiment': 'neg'},
            {'text': 'word', 'sentiment': 'neutral'}
        ]

        self.assertEqual('positive', u.getSentiment())

        u.comments = [
            {'text': 'Hola mundo', 'sentiment': 'pos'},
            {'text': 'Hello world', 'sentiment': 'neg'},
            {'text': 'Bad word', 'sentiment': 'neg'},
            {'text': 'word', 'sentiment': 'neutral'}
        ]

        self.assertEqual('negative', u.getSentiment())

        u.comments = [
            {'text': 'Hola mundo', 'sentiment': 'pos'},
            {'text': 'Hello world', 'sentiment': 'neg'},
            {'text': 'Bad word', 'sentiment': 'neutral'},
            {'text': 'word', 'sentiment': 'neutral'}
        ]

        self.assertEqual('neutral', u.getSentiment())

if __name__ == '__main__':
    unittest.main()
