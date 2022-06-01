from randomText.src.endpoints import RandomObject
from randomText.src.new_endpoints import RandomObjects2
from randomText.src.geek_endpoints import RandomObject3
from .__version__ import __version__

class RandomTextClient:
    def __init__(self, api_key=None):
        self.address = RandomObject(end_point='address/random_address')
        self.appliance = RandomObject(end_point='appliance/random_appliance')
        self.app = RandomObject(end_point='app/random_app')
        self.bank = RandomObject(end_point='bank/random_bank')
        self.beer = RandomObject(end_point='beer/random_beer')
        self.blood = RandomObject(end_point='blood/random_blood')
        self.business_credit_card = RandomObject(end_point='business_credit_card/random_card')
        self.cannabis = RandomObject(end_point='cannabis/random_cannabis')
        self.code = RandomObject(end_point='code/random_code')
        self.coffee = RandomObject(end_point='coffee/random_coffee')
        self.commerce = RandomObject(end_point='commerce/random_commerce')
        self.company = RandomObject(end_point='company/random_company')
        self.computer = RandomObject(end_point='computer/random_computer')
        self.crypto = RandomObject(end_point='crypto/random_crypto')
        self.crypto_coin = RandomObject(end_point='crypto_coin/random_crypto_coin')
        self.color = RandomObject(end_point='color/random_color')
        self.dessert = RandomObject(end_point='dessert/random_dessert')
        self.device = RandomObject(end_point='device/random_device')
        self.food = RandomObject(end_point='food/random_food')
        self.name = RandomObject(end_point='name/random_name')
        self.hipster = RandomObject(end_point='hipster/random_hipster_stuff')
        self.invoice = RandomObject(end_point='invoice/random_invoice')
        self.user = RandomObject(end_point='users/random_user')
        self.stripe = RandomObject(end_point='stripe/random_stripe')
        self.subscription = RandomObject(end_point='subscription/random_subscription')
        self.vehicle = RandomObject(end_point='vehicle/random_vehicle')
        self.id_number = RandomObject(end_point='id_number/random_id_number')
        self.internet_stuff = RandomObject(end_point='internet_stuff/random_internet_stuff')
        self.lorem_ipsum = RandomObject(end_point='lorem_ipsum/random_lorem_ipsum')
        self.lorem_flickr = RandomObject(end_point='lorem_flickr/random_lorem_flickr')
        self.lorem_pixel = RandomObject(end_point='lorem_pixel/random_lorem_pixel')
        self.nation = RandomObject(end_point='nation/random_nation')
        self.number = RandomObject(end_point='number/random_number')
        self.phone_number = RandomObject(end_point='phone_number/random_phone_number')
        self.placeholdit = RandomObject(end_point='placeholdit/random_placeholdit')
        self.restaurant = RandomObject(end_point='restaurant/random_restaurant')
        self.geek = RandomObject3()

        if api_key is not None:
            self.fancy_random = RandomObjects2(api_key=api_key)

    def __str__(self):
        return f'RandomTextClient {__version__}'