from app import books

USER_CHOICE = '''
Enter one of the following:
- 'b' to look at 5 star books
- 'c' to look at the cheapest books
- 'n' to get the next available book
- 's' to search by book title
- 'q' to quit
enter your choice: '''

original_books = books.copy()

def search_books_by_keyword():
    keyword = input("Enter a keyword to search in book titles: ")
    matching_books = [book for book in original_books if keyword.lower() in book.name.lower()]

    if matching_books:
        for book in matching_books:
            print(book)
    else:
        print(f"No books found with the keyword '{keyword}'.")


# gets the 10 books with the best rating
def print_best_books():
    best_books = sorted(original_books, key=lambda x: x.rating, reverse=True)[:10]
    for book in best_books:
        print(book)


# gets the 10 cheapest books
def print_cheapest_books():
    cheapest_books = sorted(original_books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)

def get_next_book():
    print(next(books_generator))



def menu():
        while True:
            user_input = input(USER_CHOICE)

            if user_input == "q":
                break

            elif user_input == "b":
                print_best_books()

            elif user_input == "c":
                print_cheapest_books()

            elif user_input == "n":
                get_next_book()

            elif user_input == "s":
                search_books_by_keyword()

            else:
                print("invalid option")

menu()

