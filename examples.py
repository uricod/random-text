from randomText import RandomTextClient
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    api_key = os.getenv('API_KEY')

    client = RandomTextClient(api_key=api_key)
    response = client.coffee.get_random(size=5)
    print(response)

    business_name = client.fancy_random.generate_business_name(size=2)
    print(business_name)

    brand_name = client.fancy_random.generate_brand_name(starting_word='funny')
    print(brand_name)

    product_reviews = client.fancy_random.generate_product_reviews(size=2, product='toy')
    print(product_reviews)

if __name__ == '__main__':
    main()