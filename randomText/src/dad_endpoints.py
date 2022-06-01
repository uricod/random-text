from randomText.src.base_dad import DadJoke
import pandas as pd


class RandomObject5(DadJoke):
    def __init__(self):
        super().__init__()

    def get_dad_joke(self):
        """
        Get a random of objects
        :return: df of joke
        """
        method = 'GET'
        url = ''
        parameters = {}
        body = None
        return self.make_request(url, method, parameters, body)

    def search_dad_jokes(self, page=1, limit=20, term=''):
        """
        Get a random of objects

        :param page: page to return
        :param limit: number of items to return
        :param term: search term
        :return: df of jokes
        """
        method = 'GET'
        url = 'search'
        parameters = {'page': int(page), 'limit': int(limit), 'term': term}
        body = None
        response = self.make_request(url, method, parameters, body)
        results = pd.DataFrame(response['results'].iloc[0])
        return results
