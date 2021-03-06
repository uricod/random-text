from randomText import RandomTextClient
from dotenv import load_dotenv
import os

from randomText.src.base_testimonial import Testimonial

load_dotenv()

def main():
    api_key = os.getenv('API_KEY')

    client = RandomTextClient(api_key=api_key)
    response = client.placeholdit.get_random(size=5)
    print(response)

    lorem_pixel = client.lorem_pixel.get_random(size=5)
    print(lorem_pixel)

    business_name = client.fancy_random.generate_business_name(size=2)
    print(business_name)

    brand_name = client.fancy_random.generate_brand_name(starting_word='funny')
    print(brand_name)

    product_reviews = client.fancy_random.generate_product_reviews(size=2, product='toy')
    print(product_reviews)

    joke = client.geek.get_joke()
    print(f"Joke: {joke.iloc[0]['joke']}")

    insult = client.evil.generate_insult()
    print(f"Insult: {insult.iloc[0]['insult']} shown {insult.iloc[0]['shown']} times")

    dad_joke = client.dad.get_dad_joke()
    print(f"Dad joke: {dad_joke.iloc[0]['joke']}")

    dad_jokes = client.dad.search_dad_jokes(page=1, limit=2, term='cat')
    print(dad_jokes.head(2))

    shibe_images = client.shibe.generate_images(size=1)
    print(shibe_images.head(5))

    testimonials = client.testimonial.generate_random()
    print(testimonials.head(5))

    paragraphs = client.meta.get_paragraphs(size=2)
    print(paragraphs.head(5))

    sentences = client.meta.get_sentences(size=2)
    print(sentences.head(5))

    doc = client.meta.get_doc(paragraph_size=5, sentence_size=2)
    print(doc.head(5))

    texts = client.faker.get_texts(size=2, characters=750, country='en_US')
    print(texts.head(5))

    products = client.faker.get_products(size=2, price_min=1.00, price_max=15.00, taxes=5, country='en_US')
    print(products.head(5))
    
    persons = client.faker.get_persons(size=2, gender='male', country='en_US')
    print(persons.head(5))

    images = client.faker.get_images(size=2, type='any', width=680, height=480)
    print(images.head())



if __name__ == '__main__':
    main()