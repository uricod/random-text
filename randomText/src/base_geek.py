import requests
from pandas import json_normalize
import pandas as pd

class BaseGeek:

    def __init__(self):
        self.BASE_URL = f'https://geek-jokes.sameerkumar.website/api'

    def make_request(self, method, parameters=None, body=None):
        header = {'Content-type': 'application/json'}
        if method == 'GET':
            result = requests.get(self.BASE_URL, headers=header, params=parameters)
        elif method == 'POST':
            result = requests.post(self.BASE_URL, headers=header, json=body)
        
        if result.status_code == 200:
            df =  json_normalize(result.json())
            if len(df) == 0:
                df = pd.DataFrame({'no data': ['no data returned']})

        elif result.status_code == 401:
            df = pd.DataFrame({'error': ['unauthorized 401 - invalid api key']})
        
        elif result.status_code == 404:
            df = pd.DataFrame({'error': ['api url is not formed correctly - error 404']})

        elif result.status_code == 500:
            df = pd.DataFrame({'error': [result.json()['message']]})
        
        return df