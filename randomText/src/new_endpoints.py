from randomText.src.base_randommer import BaseRandommer

class RandomObjects2(BaseRandommer):
    def __init__(self, api_key):
        super().__init__(api_key=api_key)

    def generate_business_name(self, size, culture='en_US'):
        """
        Get a random business name based off culture
        :param size: number of items to return
        :param culture: culture to use for the name
        :return:
        """
        url = 'Name/BusinessName'
        method = 'POST'
        parameters = {'number': int(size)}
        if culture is not None:
            parameters['cultureCode'] = culture
        body = None
        return self.make_request(url, method, parameters, body)

    def generate_brand_name(self, starting_word='and'):
        """
        Get a random business name
        :param size: number of items to return
        :return:
        """
        url = 'Name/BrandName'
        method = 'POST'
        parameters = {'startingWords': str(starting_word)}
        body = None
        return self.make_request(url, method, parameters, body)
    
    def generate_product_reviews(self, size, product='toy'):
        """
        Get a random product reviews
        :param size: number of items to return
        :param product: product to use for reviews
        :return:
        """
        url = 'Text/Review'
        method = 'POST'
        parameters = {'quantity': int(size)}
        if product is not None:
            parameters['product'] = product
        body = None
        return self.make_request(url, method, parameters, body)