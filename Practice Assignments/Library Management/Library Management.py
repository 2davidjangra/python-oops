class Book:

    def __init__(self, title):
        self.title = title
        self.issued = False


class Member:

    def __init__(self, name):
        self.name = name


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, title):

        for book in self.books:

            if book.title == title and not book.issued:
                book.issued = True
                print(title, "Issued Successfully")
                return

        print("Book Not Available")

    def return_book(self, title):

        for book in self.books:

            if book.title == title and book.issued:
                book.issued = False
                print(title, "Returned Successfully")
                return

        print("Book Not Found")

    def display_books(self):

        print("\nAvailable Books:")

        for book in self.books:
            if not book.issued:
                print(book.title)


library = Library()

library.add_book(Book("Python Programming"))
library.add_book(Book("Data Structures"))
library.add_book(Book("Machine Learning"))

library.display_books()

library.issue_book("Python Programming")

library.display_books()

library.return_book("Python Programming")

library.display_books()
