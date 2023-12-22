import re
import logging
from bs4 import BeautifulSoup

from locators.all_book_locators import BooksPageLocators
from parsers.book_parser import BookParser

logger = logging.getLogger('scraping.book_page') # child logger, inherits settings and is related to the main one

class BooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = BooksPageLocators.BOOKS
        logger.debug(f'Finding all books in the page using {BooksPageLocators.BOOKS}')
        
        books = self.soup.select(locator)
        return (BookParser(e) for e in books)
    
    @property
    def page_count(self):
        logger.debug('Finding all number of pages available ...')

        content = self.soup.select_one(BooksPageLocators.PAGER).string

        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)

        pages = int(matcher.group(1))
        logger.info(f'Number of pages found: {pages}')
        return pages 