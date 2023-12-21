import requests
from itertools import chain
import logging
from pages.book_page import BooksPage

logging.basicConfig(
    format='%s:%(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)

logger = logging.getLogger('scraping')

logger.info('Loading books list ...')

page_content = requests.get("http://books.toscrape.com").content

page = BooksPage(page_content)

books = page.books

for page_num in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num + 1}.html'
    page_content = requests.get(url).content
    logger.debug("Creating BooksPage from page_content ...")
    page = BooksPage(page_content)
    books = list(chain(books, page.books))  # Convert the chain object to a list, so it can be copied in menu.py

# Now 'books' is a list containing all items from the original 'books' and the new 'page.books'
