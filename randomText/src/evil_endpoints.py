from randomText.src.base_evil import BaseEvil

class RandomObject4(BaseEvil):
    def __init__(self):
        super().__init__()

    def generate_insult(self):
        """
        Get a random of objects
        :param lang: language to return
        :param type: response type
        :return: df of insult
        """
        method = 'GET'
        parameters = {'lang': 'en', 'type': 'json'}
        body = None
        return self.make_request(method, parameters, body)