from randomText.src.base_random import BaseRandomText

class RandomObject(BaseRandomText):
    def __init__(self, end_point):
        super().__init__()
        self.END_POINT = end_point

    def get_random(self, size, is_xml=False):
        """
        Get a random of objects
        :param size: number of object examples to return
        :param is_xml: just here for consistency but doesn't change anything
        :return:
        """
        method = 'GET'
        parameters = {'size': size, 'is_xml': is_xml}
        body = None
        return self.make_request(self.END_POINT, method, parameters, body)
    
    