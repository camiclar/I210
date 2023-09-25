# 11.2 valid zip

# Part 1
# write a function valid_zip that takes an user-entered string and
# checks to see if it is 5 characters long
# note: len() will work on strings, but not integers
# returns True or False
def valid_zip(code):
    return len(code) == 5

# Part 2
# write a function find_zip that takes a user-entered string
# first checks to see if that integer is a valid zip code
# if it is, it returns a string with location information
# (you may need to convert it to an integer)
# if it is not, it returns an empty string



# main
# input - get a zip code from the user
zip_code = input("Please enter your zip code: ")

# Part 1
# processing - make sure the zip is valid
answer = valid_zip(zip_code)

# Part 2
# get some location info

# Part 1
# output whether the zip code is valid (True or False)
print("Is this a valid zip code?", answer)

# Part 2
# output - print out a special message


