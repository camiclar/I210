# 26.1 Patron
# init method
# Attributes: name, book_list ([]), is_checked_out (T/F)
# Other Methods:
# to-string
# get_name, get_book_list, get_is_checked_out, clear_book_list
# set_name, add_book_to_list, set_is_checked_out

class Patron:
    def __init__(self, name)










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
