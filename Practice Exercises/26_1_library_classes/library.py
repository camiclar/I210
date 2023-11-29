# 26.1 Library
# Attributes: all_books, all_patrons
# Methods:
# add_book, get_books, list_all_books (status 'available' or 'not available')
# add_patron, get_patrons, list_all_patrons (status 'checked out' or 'still browsing')

from book import *
from patron import *

class Library:
    def __init__(self, all_books=[], all_patrons=[]):
        self.__all_books = all_books
        self.__all_patrons = all_patrons
    
    def get_books(self):
        return self.__all_books
    
    def get_patrons(self):
        return self.__all_patrons
    
    def add_book(self, new_book):
        self.__all_books.append(new_book)

    def add_patron(self, new_patron):
        self.__all_patrons.append(new_patron)
    
    def list_all_books(self):
        for book in self.__all_books:
            print(book)
    
    def list_all_patrons(self):
        for patron in self.__all_patrons:
            print(patron)

if __name__ == "__main__":
    # testing
    # these lists will hold objects
    book1 = Book("Rambo", "Bill")
    book2 = Book("Cats", "Bilbo")
    book3 = Book()
    patron1 = Patron("Sue")

    my_library = Library()
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    my_library.add_patron(patron1)

    my_library.list_all_books()
    my_library.list_all_patrons()


    # but let's test that the interaction works internally first
    """ Library.add_book(["A Darker Shade of Magic", "Victoria Schwab"])
    Library.add_book(["A Gathering of Shadows", "Victoria Schwab"])
    Library.add_book(["A Conjuring of Light", "Victoria Schwab"])
    Library.add_patron("Holly Black")

    print(Library.get_books())
    print(Library.get_patrons())

    print(Library.list_all_books())
    print(Library.list_all_patrons()) """


# output should look like this:
# [['A Darker Shade of Magic', 'Victoria Schwab'], ['A Gathering of Shadows', 'Victoria Schwab'], ['A Conjuring of Light', 'Victoria Schwab']]
# ['Holly Black']

# ALL LIBRARY BOOKS:

# A Darker Shade of Magic
# Victoria Schwab
# Available

# A Gathering of Shadows
# Victoria Schwab
# Available

# A Conjuring of Light
# Victoria Schwab
# Available


# LIBRARY PATRONS:

# Holly Black
# Status: checked out
