import requests
import pandas as pd

class BaseRandommer:

    def __init__(self, api_key):
        self.BASE_URL = f'https://randommer.io/api/'
        self.API_KEY = api_key

    def make_request(self, url, method, parameters=None, body=None):
        header = {'X-api-key': self.API_KEY}
        if method == 'GET':
            result = requests.get(self.BASE_URL + url, headers=header, params=parameters)
        elif method == 'POST':
            result = requests.post(self.BASE_URL + url, headers=header, params=parameters)
        
        if result.status_code == 200:
            df = pd.DataFrame(result.json(), columns=['Generated Value'])
            if len(df) == 0:
                df = pd.DataFrame({'no data': ['no data returned']})

        elif result.status_code == 400:
            df = pd.DataFrame({'error': [f'bad request 400 - invalid parameters {result.text}']})

        elif result.status_code == 401:
            df = pd.DataFrame({'error': ['unauthorized 401 - invalid api key']})
        
        elif result.status_code == 404:
            df = pd.DataFrame({'error': ['api url is not formed correctly - error 404']})

        elif result.status_code == 500:
            df = pd.DataFrame({'error': [result.json()['message']]})
        
        return df