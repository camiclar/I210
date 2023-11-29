# 26.1 Patron
# init method
# Attributes: name, book_list ([]), is_checked_out (T/F)
# Other Methods:
# to-string
# get_name, get_book_list, get_is_checked_out, clear_book_list
# set_name, add_book_to_list, set_is_checked_out

class Patron:
    def __init__(self, name):
        self.__name = name
        self.__book_list = []
        self.__is_checked_out = False
    
    def get_name(self):
        return self.__name
    
    def get_book_list(self):
        return self.__book_list
    
    def get_is_checked_out(self):
        return self.__is_checked_out
    
    def clear_book_list(self):
        self.__book_list.clear()
    
    def set_name(self, new_name):
        self.__name = new_name
    
    def add_book_to_list(self, book):
        self.__book_list.append(book)
    
    def set_is_checked_out(self, new_is_checked_out):
        self.__is_checked_out = new_is_checked_out
    
    def __str__(self):
        output = "\n"
        output += self.__name
        output += "\n"

        for book in self.__book_list:
            output += book
            output += "\n"
        
        output += f"Checked out: {self.__is_checked_out}"

        return output










if __name__ == "__main__":
    patron1 = Patron("Hari Seldon")
    print(patron1.get_name())
    print("Checked out:", patron1.get_is_checked_out())
    
    # for testing only - this will be a list of objects
    # if we need to print the objects in our larger program
    # we may need to come back to this code later
    patron1.add_book_to_list("Foundation")
    patron1.add_book_to_list("Snow Crash")
    print(patron1.get_book_list())

    patron1.set_name("Dors Venabili")
    patron1.set_is_checked_out(True)
    print(patron1)


# output should look like this:
# Hari Seldon
# Checked out: False
# ['Foundation', 'Snow Crash']

# Dors Venabili
# Foundation
# Snow Crash
# Checked out: True
