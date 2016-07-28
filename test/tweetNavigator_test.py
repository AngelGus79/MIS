import mock
import unittest
import os
import sys

# Update python path
test_path = os.path.abspath(os.path.join(__file__, os.pardir))
project_path = os.path.abspath(os.path.join(test_path, os.pardir))
sys.path.append(project_path)

from src.tweetNavigator import tweetNavigator

class TweetNavigatorTest(unittest.TestCase):

    @mock.patch('src.tweetNavigator.Twython')
    def test_getUsers(self, mock):
        mock().search.return_value = {
            'statuses': [
                {'user': {'name': 'Juan'}},
                {'user': {'name': 'Pedro'}},
            ]
        }

        navigator = tweetNavigator('sayulita')
        self.assertEqual(['Juan', 'Pedro'], navigator.getUsers())


if __name__ == '__main__':
    unittest.main()
