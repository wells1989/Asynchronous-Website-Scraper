import re
import logging
from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, for £{self.price}, with a rating of {self.rating} stars>'
    

    @property
    def price(self):
        locator = BookLocators.PRICE
        item_price = self.parent.select_one(locator).string
    
        expression = '£([0-9]+\.[0-9]+)'
        matcher = re.search(expression, item_price) 
        float_price = float(matcher.group(1))

        logger.debug(f'found book price, {float_price}')
        
        return float(matcher.group(1))


    @property
    def name(self):
        locator = BookLocators.NAME
        return self.parent.select_one(locator).attrs["title"]


    @property
    def link(self):
        locator = BookLocators.LINK
        return self.parent.select_one(locator).attrs['href']


    @property
    def rating(self):
        locator = BookLocators.RATING
        ratings = self.parent.select_one(locator).attrs['class']
        
        accepted_ratings = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        returned_ratings = [rating for rating in ratings if rating in(accepted_ratings)]
        
        rating_number = accepted_ratings.get(returned_ratings[0])
        logger.debug(f'found book rating, {rating_number}')
        
        return rating_number
    

