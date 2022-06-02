[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://github.com/uricod/lend-saas/blob/master/LICENSE)
<img src="https://img.shields.io/github/v/release/uricod/random-text">

# **Random-Text**
A Random Object Generator for Addresses, Names, Reviews, Testimonials, Business Names, and Random Objects.

## **Sources**

| Description     | Type      | Link     |
| ------------- | ------------- | -------- |
| Random Data Website   | General | [Click](https://random-data-api.com/)  |
| Randommer Data Website | General   | [Click](https://randommer.io/) |
| Random Geek Jokes | Jokes | [Click](https://github.com/sameerkumar18/geek-joke-api)|
| Evil Insult Generator | Jokes | [Click](https://evilinsult.com/api/)|
| Dad Jokes | Jokes | [Click](https://icanhazdadjoke.com/)|
| Shibe Generator | Images | [Click](https://shibe.online/) |
| Testimonial Generator | Text | [Click](https://testimonialapi.toolcarton.com/)|
| Text Generator | Text | [Click](http://metaphorpsum.com/)|

----
> To use the Randommer API you will require a API Key. To create one is free. Follow link to  website and register as a user and you will find API Key in your "account" section.
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

#### Available Methods

| Module   | Example |Output                                     |
| -------- | --------------------------------------------- | -------------- |
| Address  | `client.address.get_random(size=5)`  | df of addresses     |
| Appliances   | `client.appliance.get_random(size=5)`   |  df of appliances |
| Apps | `client.app.get_random(size=5)` | df of apps  |
| Banks | `client.bank.get_random(size=5)` | df of banks |
| Beers | `client.beer.get_random(size=5)` | df of beers |
| Blood | `client.blood.get_random(size=5)`| df of blood types |
| Credit Cards | `client.business_credit_card.get_random(size=5)`|df of credit card numbers|
| Cannabis | `client.cannabis.get_random(size=5)` | df of cannabis data |
| Code | `client.code.get_random(size=5)` | df of code |
| Coffee | `client.coffee.get_random(size=5)` | df of coffee |
| Commerce | `client.commerce.get_random(size=5)` | df of products |
| Company | `client.company.get_random(size=5)` | df of company data |
| Computer | `client.computer.get_random(size=5)` | df of operating systems |
| Crypto | `client.crypto.get_random(size=5)` | df of Crypto hashes |
| Crypto Coin | `client.crypto_coin.get_random(size=5)` | df of crypto coins |
| Color | `client.color.get_random(size=5)` | df of colors |
| Dessert | `client.dessert.get_random(size=5)` | df of desserts |
| Devices | `client.device.get_random(size=5)` | df of phones |
| Food | `client.food.get_random(size=5)` | df of foods |
| Names | `client.name.get_random(size=5)` | df of full names |
| Hipster | `client.hipster.get_random(size=5)` | df of hipster text |
| Invoice | `client.invoice.get_random(size=5)` | df of invoice data |
| User | `client.user.get_random(size=5)` | df of user data |
| Stripe | `client.stripe.get_random(size=5)` | df of stripe financial data |
| Subscription | `client.subscription.get_random(size=5)` | df of subscriptions |
| Vehicle | `client.vehicle.get_random(size=5)` | df of vehicles |
| Id_Number | `client.id_number.get_random(size=5)` | df of id numbers - Including SSN |
| Internet Stuff | `client.internet_stuff.get_random(size=5)` | df of logins and browser info |
| Lorem Ipsum | `client.lorem_ipsum.get_random(size=5)` | df of fake text for website |
| Lorem Pixel | `client.lorem_pixel.get_random(size=5)` | df of fake image data |
| Lorem Flickr | `client.lorem_flickr.get_random(size=5)` | df of fake image from flickr |
| Nation | `client.nation.get_random(size=5)` | df of nations |
| Number | `client.number.get_random(size=5)` | df of numbers |
| Phone Number | `client.phone_number.get_random(size=5)` | df of Phone Numbers |
| Place Hold It | `client.placeholdit.get_random(size=5)` | df of placeholder images |
| Restaurant | `client.restaurant.get_random(size=5)` | df of restaurants |
| Fancy Random | `client.fancy_random.generate_business_name(size=5)` | df of fake business Names |
| Fancy Random| `client.fancy_random.generate_brand_name(starting_word='funny')` | df of brand names |
| Fancy Random | `client.fancy_random.generate_product_reviews(size=2, product='toy')` | df of product reviews |
| Geek Jokes | `client.geek.get_joke()` | df of geek jokes |
| Evil Insults | `client.evil.generate_insult()` | df of insults |
| Dad Jokes | `client.dad.get_dad_joke()` | df of dad jokes |
| Dad Jokes | `client.dad.search_dad_jokes(page=1, limit=2, term='cat')` | df of found dad jokes |
| Shibe | `client.shibe.generate_images(size=1)` | df of shibe images |
| Testimonials | `client.testimonial.generate_random()` | df of Testimonials |
| Meta | `client.meta.get_paragraphs(size=2)` | df of paragraphs |
| Meta | `client.meta.get_sentences(size=2)` | df of sentences |
| Meta | `client.meta.get_doc(paragraph_size=5, sentence_size=2)` | df of paragraphs and sentences |


#### TO DO
1. Add as many random open api's from the web. Based off https://github.com/public-apis/public-apis


#### **Tests**
To run tests:
```cmd
python -m unittest discover -p *test.py
```

#### **Disclaimer**
1. **This library depends on the source API's still working as intended. If they change or pull their resources the code will no longer work as none of the logic is done in this library but pulled from around the web.**