# 24 Encapsulated in Verona
# Create the class Person
#   - Each person should have a name, address, phone
#   - All attributes should be __private
# We should be able to get a person’s name, address and phone
# We should be able to set a new name, address or phone: (with the following limitations)
#   - Addresses should be in Italy to be valid, or print out “Invalid address”
#   - Phone numbers need to include 10 digits, or print out “Invalid number”
#       -- consider using .isdigit()

class Person:
    """Creates an person object"""

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        if address.find("Italy") != -1:
            self.__address = address
        else:
            print("Invalid address")

    def set_phone(self, phone):
        num_digits = 0
        for i in range(len(phone)):
            if phone[i].isdigit():
                num_digits += 1

        if num_digits == 10:
            self.__phone = phone
        else:
            print("Invalid number")

    def print(self):
        print(self.__name)
        print(self.__address)
        print(self.__phone)
    
    def call(self, number):
        print("Calling", number)
        if self.__phone == number:
            print("Hello?")
        else:
            print("Ring... Ring... Ring...")


if __name__ == "__main__":
    # output should match slides
    print("\nRomeo and Juliet:\n")
    # create Romeo
    romeo = Person("Romeo Montague", "Verona, Italy", "+39 045 205 0931")
    # create Juliet
    juliet = Person("Juliet Capulet", "Verona, Italy", "+39 045 595944")
    # meet Romeo
    print(romeo)
    # meet Juliet
    print(juliet)
    # Romeo meets Juliet at a party, but he's from the wrong side of the canal in Verona
    # He secretly gives her his number anyway
    print("For Jules, love R:", romeo.get_phone())
    # Romeo and Juliet hit it off, get secretly engaged
    # She updates her last name to Montague in her contacts, 
    # you know, just to see what it looks like
    juliet.set_name("Juliet Montague")
    print("J: Let's see what this looks like...", juliet.get_name())
    # Her family finds out, chases Romeo off, he hides out in Mantua 
    romeo.set_address("Mantua")
    print("R: Off to", romeo.get_address(), "...wait that's not right.")
    # oh right, in Italy
    romeo.set_address("Mantua, Italy")
    print("R: For real this time, gotta hide out in", romeo.get_address())
    # Juliet loses her phone, and gets Friar Laurence to bring her a new one 
    # Tells him to give Romeo her new number! +39 045 595600
    juliet.set_phone("+39 376 13765")
    # BUT HE GIVES ROMEO THE WRONG NUMBER
    print("Trying Juliet...")
    juliet.call("+39 045 595600")
    # when she doesn't answer he thinks Juliet is dead!!
    # if only he'd been able to check that she was still around...
    print("But she's fine, right?:", isinstance(juliet, Person))
    print()
    print(romeo)
    print(juliet)
