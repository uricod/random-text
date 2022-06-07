from randomText.src.base_faker import Faker
import pandas as pd


class RandomObject9(Faker):
    def __init__(self):
        super().__init__()

    def get_addresses(self, size=1, country='en_US'):
        """
        Get a random of objects
        :param size: number of addresses to return
        :param country: country to return addresses from
        :return: df of joke
        """
        method = 'GET'
        url = 'addresses'
        body = None
        return self.make_request(url, method, quantity=size, locale=country, body=body)

    def get_books(self, size=1, country='en_US'):
        """
        Get a random of objects
        :param size: number of books to return
        :param country: country to return addresses from
        :return: df of joke
        """
        method = 'GET'
        url = 'books'
        body = None
        return self.make_request(url, method, quantity=size, locale=country, body=body)

    def get_companies(self, size=1, country='en_US'):
        """
        Get a random of objects
        :param size: number of companies to return
        :param country: country to return addresses from
        :return: df of joke
        """
        method = 'GET'
        url = 'companies'
        body = None
        return self.make_request(url, method, quantity=size, locale=country, body=body)

    def get_credit_cards(self, size=1, country='en_US'):
        """
        Get a random of objects
        :param size: number of credit_cards to return
        :param country: country to return addresses from
        :return: df of joke
        """
        method = 'GET'
        url = 'credit_cards'
        body = None
        return self.make_request(url, method, quantity=size, locale=country, body=body)

    def get_places(self, size=1, country='en_US'):
        """
        Get a random of objects
        :param size: number of places to return
        :param country: country to return addresses from
        :return: df of joke
        """
        method = 'GET'
        url = 'places'
        body = None
        return self.make_request(url, method, quantity=size, locale=country, body=body)

    def get_users(self, size=1, country='en_US'):
        """
        Get a random of objects
        :param size: number of users to return
        :param country: country to return users from
        :return: df of joke
        """
        method = 'GET'
        url = 'users'
        body = None
        return self.make_request(url, method, quantity=size, locale=country, body=body)

    def get_texts(self, size=1, characters=350, country='en_US'):
        """
        Get a random of objects
        :param size: number of credit_cards to return
        :param characters: number of characters to return
        :param country: country to return addresses from
        :return: df of joke
        """
        method = 'GET'
        url = 'texts'
        params = {'_characters': characters}
        body = None
        return self.make_request(url, method, quantity=size, locale=country, other_parameters=params, body=body)

    def get_products(self, size=1, price_min=0.01, price_max=10.35, taxes=25, categories_type='', country='en_US'):
        """
        Get a random of objects
        :param size: number of credit_cards to return
        :param price_min: minimum price to return - float 10.35
        :param price_max: maximum price to return - float 10.35
        :param taxes: taxes to return - percentage 25
        :param categories_type: categories to return - string uuid number. 
        :param country: country to return addresses from
        :return: df of joke
        """
        method = 'GET'
        url = 'products'
        params = {'_price_min': price_min, '_price_max': price_max, '_taxes': taxes, '_categories_type': categories_type}
        body = None
        return self.make_request(url, method, quantity=size, locale=country, other_parameters=params, body=body)

    def get_persons(self, size=1, gender='male', birthday_start='1991-01-01', birthday_end='2022-01-01', country='en_US'):
        """
        Get a random of objects
        :param size: number of credit_cards to return
        :param gender: male or female
        :param birthday_start _birthday_start=1994-02-09
        :param birthday_end _birthday_end=2018-10-09
        :param country: country to return addresses from
        :return: df of joke
        """
        method = 'GET'
        url = 'persons'
        params = {'_gender': gender, '_birthday_start': birthday_start, '_birthday_end': birthday_end}
        body = None
        return self.make_request(url, method, quantity=size, locale=country, other_parameters=params, body=body)

    def get_images(self, size=1, type='any', width='640', height='480', country='en_US'):
        """
        Get a random of objects
        :param size: number of credit_cards to return
        :param type: any, animals, architecture, nature, people, tech, kittens, pokemon
        :param width: width to return - int 640
        :param height: height to return - int 480
        :param country: country to return addresses from
        :return: df of joke
        """
        method = 'GET'
        url = 'images'
        params = {'_type': type, '_width': width, '_height': height}
        body = None
        return self.make_request(url, method, quantity=size, locale=country, other_parameters=params, body=body)

