from randomText.src.base_geek import BaseGeek

class RandomObject3(BaseGeek):
    def __init__(self):
        super().__init__()

    def get_joke(self):
        """
        Get a random of objects
        :param size: number of object examples to return
        :param is_xml: just here for consistency but doesn't change anything
        :return:
        """
        method = 'GET'
        parameters = {'format': 'json'}
        body = None
        return self.make_request(method, parameters, body)