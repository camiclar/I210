# 26.1 Library
# Attributes: all_books, all_patrons
# Methods:
# add_book, get_books, list_all_books (status 'available' or 'not available')
# add_patron, get_patrons, list_all_patrons (status 'checked out' or 'still browsing')

class Library:










if __name__ == "__main__":
    # testing
    # these lists will hold objects
    # but let's test that the interaction works internally first
    Library.add_book(["A Darker Shade of Magic", "Victoria Schwab"])
    Library.add_book(["A Gathering of Shadows", "Victoria Schwab"])
    Library.add_book(["A Conjuring of Light", "Victoria Schwab"])
    Library.add_patron("Holly Black")

    print(Library.get_books())
    print(Library.get_patrons())

    print(Library.list_all_books())
    print(Library.list_all_patrons())


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
