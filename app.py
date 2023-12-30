import requests
from itertools import chain
import logging
from pages.book_page import BooksPage
import aiohttp
import asyncio
import time

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

# asynchronous requests

loop = asyncio.get_event_loop()

async def fetch_page(session, url):
    page_state = time.time()
    async with asyncio.timeout(10):
        async with session.get(url) as response:
                print(f'page took {time.time() - page_state}')
                return await response.text()
    # each fetch_page has a timeout(10 seconds) and awaits the response, so others can run concurrently, and returns response text aka html content

async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)

        return await grouped_tasks # returned as individual elements in a list of results of all the tasks that were ran, i.e. a list of html content from each page
    # above, opens a session, and for each url runs the fetch_page function (concurrently) and then .gather awaits all tasks to be completed before proceeding

urls = [f'http://books.toscrape.com/catalogue/page-{page_num + 1}.html' for page_num in range(1, page.page_count)]

start = time.time()

pages = loop.run_until_complete(get_multiple_pages(loop, *urls)) # i.e. runs the fetch_page for each url, using the event loop

print(f'took {time.time() - start}')

for page_content in pages:
    page = BooksPage(page_content)
    books = list(chain(books, page.books)) # adds the BookPage content from each page to the books list
