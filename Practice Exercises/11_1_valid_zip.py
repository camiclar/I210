# 11.1 valid zip

# Part 1
# write a function valid_zip that takes an user-entered string and
# checks to see if it is 5 characters long
# note: len() will work on strings, but not integers
# returns True or False
def is_valid_zip(zipcode):
    if len(zipcode) == 5:
        return True
    else:
        return False
    
def is_in_Bloomington(zipcode):
    if int(zipcode) >= 47401 and int(zipcode) <= 47408:
        return "Bloomington"
    else:
        return "your hometown"

# main
# input - get a zip code from the user
zip_code = input("Please enter your zip code: ")

# Part 1
# processing - make sure the zip is valid
is_valid = is_valid_zip(zip_code)

# Part 1
# output whether the zip code is valid (True or False)

if is_valid:
    print(f"How's the weather in {is_in_Bloomington(zip_code)}?")
else:
    print("Not a valid zip code")
