# Book Website Scraper: 

A site to scrape key information using requests / BeautifulSoup library on HTML websites

## Project Requirements

Python 3.11.1

```python
autopep8==2.0.4
bcrypt==4.0.1
beautifulsoup4==4.12.2
black==23.12.0
certifi==2023.11.17
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
idna==3.6
mypy-extensions==1.0.0
packaging==23.2
pathspec==0.12.1
platformdirs==4.1.0
pycodestyle==2.11.1
requests==2.31.0
soupsieve==2.5
urllib3==2.1.0
```

## Usage

```python
BooksPage class:

BooksPage.books
    # returns a BookParser instance for each book

BooksPage.page_count
    # uses regex to get the number of available pages in the site, to allow simultaneous page loading
```

```python
BookParser class:

BookParser.price    
    # uses regex to find a float of the book price

BookParser.name    
    # returns the book title

BookParser.link    
    # returns the href url link in each book

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
- Logging was used throughout to assist with debugging at various points of development
