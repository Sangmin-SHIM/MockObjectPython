import unittest
from datetime import datetime
from unittest.mock import Mock
from requests import Timeout
from unittest import TestCase

# Set test days
monday = datetime(year=2022, month=5, day=30)
saturday = datetime(year=2022, month=6, day=4)

# Mock
datetime = Mock()

# Function
def is_weekday():
    today = datetime.today()
    return (0<= today.weekday() < 5)

# Mock .today() to return Monday
datetime.today.return_value = monday
# Test Monday
assert is_weekday()

# Mock .today() to return Saturday
datetime.today.return_value = saturday
# Test Monday
assert not is_weekday()

# Mock
requests = Mock()

def get_holidays():
    request = requests.get('http://localhost/api/holidays')
    if request.status_code == 200:
        return request.json()
    return None

class TestCalendar(TestCase):
    def test_get_holidays_timeout(self):
        requests.get.side_effect = requests.exceptions.Timeout
        with self.assertRaises(requests.exceptions.Timeout):
            get_holidays()

if __name__ == '__main__':
    unittest.main()