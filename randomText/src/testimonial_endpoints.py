from randomText.src.base_testimonial import Testimonial

class RandomObject7(Testimonial):
    def __init__(self):
        super().__init__()

    def generate_random(self):
        """
        Get a random of objects
        :param size: count of how many to return (max 10)
        :return: df of testimonials
        """
        method = 'GET'
        parameters = {}
        body = None
        return self.make_request(method, parameters, body)