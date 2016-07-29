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
from src.statistics import Statistics


class TweetNavigatorTest(unittest.TestCase):

    def test_getUsersCount(self):
        juan = User(name='Juan')
        juan.gender = 'male'

        fatima = User(name='Fatima')
        fatima.gender = 'female'

        pedro = User(name='Pedro')
        pedro.gender = 'male'

        users = {
            '1234': juan,
            '1010': fatima,
            '2222': pedro,
        }

        s = Statistics(users)
        counts = s.getUsersCount()
        self.assertEqual(2, counts['male'])
        self.assertEqual(1, counts['female'])
        self.assertEqual(0, counts['undefined'])
        self.assertEqual(3, counts['total'])

if __name__ == '__main__':
    unittest.main()
