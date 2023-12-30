# Book Website Scraper: 

A site to scrape key information using requests / BeautifulSoup library on HTML websites

## Project Requirements

Python 3.11.1

```python
aiohttp==3.9.1
aiosignal==1.3.1
asyncio==3.4.3
attrs==23.1.0
beautifulsoup4==4.12.2
certifi==2023.11.17
charset-normalizer==3.3.2
frozenlist==1.4.1
idna==3.6
multidict==6.0.4
requests==2.31.0
soupsieve==2.5
urllib3==2.1.0
yarl==1.9.4
```

## Usage

```python
BooksPage class:

@property
BooksPage.books
    # returns a BookParser instance for each book

@property
BooksPage.page_count
    # uses regex to get the number of available pages in the site, to allow simultaneous page loading
```

```python
BookParser class:

@property
BookParser.price    
    # uses regex to find a float of the book price

@property
BookParser.name    
    # returns the book title

@property
BookParser.link    
    # returns the href url link in each book

@property
BookParser.rating    
    # Scrapes the rating from the class attribute and returns it as an integer
```


menu.py (user UI Menu)
```python

def print_best_books():
# returns list of highest rated books

def print_cheapest_books():
# returns list of cheapest books

def get_next_book():
# book generator that produces the next available book

def search_books_by_keyword():
# allows a user to search by book title
```

## Personal notes
- This was a project aiming to practice and deepen my understanding on web scraping using Python, hence the methods and structure is specific to the website used in app.py
- The focus of this project was to a/ implement web scraping with python and b/ make the code more efficient by implementing asynchronous requests
- Logging was used throughout to assist with debugging at various points of development
