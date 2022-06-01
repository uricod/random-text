[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://github.com/uricod/lend-saas/blob/master/LICENSE)
<img src="https://img.shields.io/github/v/release/uricod/random-text">

# **Random-Text**
A Random Object Generator for Addresses, Names, Reviews, Business Names, and Random Objects.

## **Sources**
- [Random Data Website](https://random-data-api.com/)
- [Randommer Data Website](https://randommer.io/)
- [Random Geek Jokes](https://github.com/sameerkumar18/geek-joke-api)
- [Evil Insult Generator](https://evilinsult.com/api/)
- [Dad Jokes](https://icanhazdadjoke.com/)


1. For an overview of the Random Data API, [click here]( https://random-data-api.com/documentation).
1. For an overview of the Randommer.io API [click here]( https://randommer.io/randommer-api)
1. For an Overview of Random Geek Jokes, see above link.
1. For an Overview of Evil Insult Generator see above link.
1. For an Overview of Dad Jokes API [click here](https://icanhazdadjoke.com/api)

----
To use the second api you will require a API Key. To create one is free. Go to above website and register as a user and you will find API Key in your "account" section.
Don't forget to pass in the API key to the RandomTextClient if you want to use the second generator.

#### **Requirements**
- Python >= 3.6

#### **Getting started**
`pip install random-text`

`random-text` is simple to use -- take a look at the below example:
```python
from randomText import RandomTextClient

client = RandomTextClient(api_key='api_key')
```

**Available methods:**
#### Basic Usage (No Api Key Required)
```python
df = client.address.get_random(size=1)
print(df.head(2))
```

#### Advanced Usage - Requires API Key when creating the client.
```python
business_name = client.fancy_random.generate_business_name(size=2)
brand_name = client.fancy_random.generate_brand_name(starting_word='funny')
product_reviews = client.fancy_random.generate_product_reviews(size=2, product='toy')
```

**Available Objects:**
1. Address
1. Appliances
1. Apps
1. Banks
1. Beers
1. Blood
1. Credit Card
1. Cannabis
1. Code
1. Coffee
1. Commerce
1. Company
1. Computer
1. Crypto
1. Crypto Coin
1. Color
1. Dessert
1. Device
1. Food
1. Dessert
1. Device
1. Name
1. Hipster
1. Invoice
1. User
1. Stripe
1. Subscription
1. Vehicle
1. Id_Number
1. Internet Stuff
1. Lorem Ipsum
1. Lorem Pixel
1. Lorem Flickr
1. Nation
1. Number
1. Phone Number
1. Place Hold It
1. Restaurant
1. Fancy Random
1. Geek Jokes
1. Evil Insults
1. Dad Jokes

#### TO DO
Add GraphQL option for above API.
Add more random data from this api: https://randommer.io/randommer-api

#### **Tests**
To run tests:
```cmd
python -m unittest discover -p *test.py
```