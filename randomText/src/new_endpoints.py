from randomText.src.base_randommer import BaseRandommer

class RandomObjects2(BaseRandommer):
    def __init__(self, api_key):
        super().__init__(api_key=api_key)

    def generate_business_name(self, size):
        """
        Get a random address
        :param size: number of items to return
        :return:
        """
        url = 'Name/BusinessName'
        method = 'POST'
        parameters = {'number': int(size)}
        body = None
        return self.make_request(url, method, parameters, body)