# 13.3 valid zip update

def valid_zip(is_zip):
    # update: checks to see: 
    #   if zip code is 5 characters long OR 10 characters long
    #   if zip is 5 -- make sure it's all digits
    #   if zip is 10 -- make sure it's 5 digits, one + sign, and 4 digits
    
    is_valid = False
    if len(is_zip) == 5:
        is_valid = is_zip.isdigit()
    elif len(is_zip) == 10:
        is_valid = is_zip[0:4].isdigit() and is_zip[5] == "+" and is_zip[6:].isdigit()
    
    return is_valid
    

# customized location info for each valid zip code
def find_zip(is_zip):
    if not valid_zip(is_zip):
        return "That's not a valid zip code."

    # update: checks only the base zipcode a.k.a. the first five numbers
    if 47401 <= int(is_zip[0:5]) <= 47408:
        zone = "Bloomington"
    else:
        zone = "your hometown"

    return zone

# main
# take zipcode in as a string to start - convert to int() when needed
zip_code = input("Please enter your zip code: ")

location = find_zip(zip_code)

if location:
    print("How's the weather in" , location + "?")
else: 
    print("That's not a valid zip code.")

