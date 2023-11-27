# 26.1 Book
# init method
# Attributes: title, author, is_available (boolean)
# Other Methods:
# get_title, get_author, get_is_available
# set_title, set_author, set_is_available
# to-string method - output example below

class Book:
    def __init__(self, title="None", author="None", is_available=True):
        self.__title = title
        self.__author = author
        self.__is_available = is_available

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_is_available(self):
        return self.__is_available

    def set_title(self, new_title):
        self.__title = new_title

    def set_author(self, new_author):
        self.__author = new_author

    def set_is_available(self, new_is_available):
        self.__is_available = new_is_available

    def __str__(self):
        output = ""
        output += self.__title
        output += "\n"
        output += self.__author
        output += "\n"

        if self.__is_available:
            output += "This book is currently available."
        else:
            output += "This book is checked out."

        output += "\n"

        return output



if __name__ == "__main__":
    book1 = Book()
    book1.set_title("The Dispossessed")
    book1.set_author("Ursula LeGuin")
    print(book1)
    print("Description:\nMust read author {} was well-known for her uptopian novel {} about anarchy and other societal structures. The book is part of a cycle of award-winning novels, the most famous of which is 'The Left Hand of Darkness.'{}'s Earthsea trilogy was revolutionary when it was released in 1968, not only for its portrayal of islands full of people who aren't white by a female fantasy and science fiction author, but also for her treatment of magic as a balance of power and responsibility.\n".format(book1.get_author(), book1.get_title(), book1.get_author()))

    book2 = Book()
    book2.set_title("Wool")
    book2.set_author("Hugh Howey")
    book2.set_is_available(False)
    print(book2)

    book2.set_title("A Plague of Giants")
    book2.set_author("Kevin Hearne")
    book2.set_is_available(True)
    book2.get_is_available()
    print(book2)


# Output should look like this:
# The Dispossessed
# Ursula LeGuin
# This book is currently available.

# Description:
# Must read author Ursula LeGuin was well-known for her uptopian novel The Dispossed about anarchy and other societal structures. The book is part of a cycle of award-winning novels, the most famous of which is 'The Left Hand of Darkness.'Ursula LeGuin's Earthsea trilogy was revolutionary when it was released in 1968, not only for its portrayal of islands full of people who aren't white by a female fantasy and science fiction author, but also for her treatment of magic as a balance of power and responsibility.

# Wool
# Hugh Howey
# This book is checked out.

# A Plague of Giants
# Kevin Hearne
# This book is currently available.
