import mock
import unittest
import os
import sys

# Update python path
test_path = os.path.abspath(os.path.join(__file__, os.pardir))
project_path = os.path.abspath(os.path.join(test_path, os.pardir))
sys.path.append(project_path)

from src.tweetNavigator import tweetNavigator, User


class TweetNavigatorTest(unittest.TestCase):

    @mock.patch('src.tweetNavigator.Twython')
    def test_getUsers(self, mock):
        mock().search.return_value = {
            'statuses': [
                {
                    'user': {'name': 'Juan'},
                    'text': 'Hola',
                    'id_str': '1122'
                },
                {
                    'user': {'name': 'Pedro'},
                    'text': 'Adios',
                    'id_str': '1234'
                },
            ]
        }

        navigator = tweetNavigator('sayulita')
        users = navigator.getUsers()

        self.assertEqual(2, len(users))
        user = users['1122']
        self.assertIsInstance(user, User)
        self.assertEqual('Juan', user.name)
        self.assertEqual(['Hola'], user.comments)


if __name__ == '__main__':
    unittest.main()
