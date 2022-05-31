[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://github.com/uricod/lend-saas/blob/master/LICENSE)
<img src="https://img.shields.io/github/v/release/uricod/random-text">

# **Random-Text**
A Random Object Generator for Addresses and the likes.
[Random Data Website](https://random-data-api.com/)


For an overview of the Random Data API, [click here]( https://random-data-api.com/documentation).


#### **Requirements**
- Python >= 3.6

#### **Getting started**
`pip install random-text`

`random-text` is simple to use -- take a look at the below example:
```python
from randomText import RandomTextClient

client = RandomTextClient()
```

**Available methods:**
#### get_random(size='how many to return')
```python
df = client.address.get_random(size=1)
print(df.head(2))
```

**Available Objects:**
1. **Address**
1. **Appliances**
1. **Apps**
1. **Banks**
1. **Beers**
1. **Blood**
1. **Credit Card**
1. **Cannabis**
1. **Code**
1. **Coffee**
1. **Commerce**
1. **Company**
1. **Computer**
1. **Crypto**
1. **Crypto Coin**
1. **Color**
1. **Dessert**
1. **Device**
1. **Food**
1. **Dessert**
1. **Device**
1. **Name**
1. **Hipster**
1. **Invoice**
1. **User**
1. **Stripe**
1. **Subscription**
1. **Vehicle**
1. **Id_Number**
1. **Internet Stuff**
1. **Lorem Ipsum**
1. **Lorem Pixel**
1. **Lorem Flickr**
1. **Nation**
1. **Number**
1. **Phone Number**
1. **Place Hold It**
1. **Restaurant**

#### TO DO
Add GraphQL option

#### **Tests**
Not working as of yet