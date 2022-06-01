from randomText.src.base_geek import BaseGeek

class RandomObject3(BaseGeek):
    def __init__(self):
        super().__init__()

    def get_joke(self):
        """
        :return: df of joke:
        """
        method = 'GET'
        parameters = {'format': 'json'}
        body = None
        return self.make_request(method, parameters, body)