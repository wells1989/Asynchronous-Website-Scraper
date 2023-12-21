from app import books

USER_CHOICE = '''
Enter one of the following:
- 'b' to look at 5 star books
- 'c' to look at the cheapest books
- 'n' to get the next available book
- 'q' to quit
enter your choice: '''

original_books = books.copy() # need a copy, otherwise the sorting functions will sort the same list permanently

def print_best_books():
    best_books = sorted(original_books, key=lambda x: x.rating, reverse=True)[:10] # sorts by the x.rating property, first 10 indexes
    for book in best_books:
        print(book)

def print_cheapest_books():
    cheapest_books = sorted(original_books, key=lambda x: x.price)[:10] # sorts by the price, cheapest 10
    for book in cheapest_books:
        print(book)

# sorting by 2 factors, e.g. sorts by first then if any match, sorts by 2nd, e.g. best_cheapest_books = sorted(books, key=lambda x: (x.rating * -1, x.price))

books_generator = (x for x in books)
# above alt to looping / using len etc as books doesn't have a len property, generators don't need it as they generate on the fly

def get_next_book():
    print(next(books_generator))
# just prints the books out 1 after another


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

            else:
                print("invalid option")

menu()

