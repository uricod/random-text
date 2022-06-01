from randomText.src.base_shibe import Shibe

class RandomObject6(Shibe):
    def __init__(self):
        super().__init__()

    def generate_images(self, size=1):
        """
        Get a random of objects
        :param size: count of how many to return
        :return: df of image links
        """
        method = 'GET'
        parameters = {'count': int(size)}
        body = None
        return self.make_request(method, parameters, body)