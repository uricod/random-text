import unittest
from randomText import RandomTextClient
import unittest
import pandas as pd

class TestAPI(unittest.TestCase):
    def test_base_object(self):
        api_key = '12345'
        client = RandomTextClient(api_key=api_key)
        response = client.coffee.get_random(size=5)
        self.assertIsInstance(response, pd.DataFrame, msg='Response is not a DataFrame')
