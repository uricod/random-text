from randomText.src.base_random import BaseRandomText

class RandomObject(BaseRandomText):
    def __init__(self, end_point):
        super().__init__()
        self.END_POINT = end_point

    def get_random(self, size, is_xml=False):
        """
        Get a random address
        :param size: number of addresses to return
        :param is_xml: return xml or json
        :return:
        """
        method = 'GET'
        parameters = {'size': size, 'is_xml': is_xml}
        body = None
        return self.make_request(self.END_POINT, method, parameters, body)
    
    