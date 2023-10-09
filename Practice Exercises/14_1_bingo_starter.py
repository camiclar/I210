# 14 Bingo
# Write a program that creates then chooses bingo combinations
import copy, random

# OVERVIEW OF BINGO:
# 75-ball Bingo Cards
# https://youtu.be/dJ4YDTqmhJk - Not familiar with the game? Start here.
# Players use cards that feature five columns of five squares each, 
# with every square containing a number (except the middle square, 
# which is designated a free "BINGO" space). 
# The columns are labeled "B" (numbers 1–15), "I" (numbers 16–30), 
# "N" (numbers 31–45), "G" (numbers 46–60), and "O" (numbers 61–75)

# Write a function that creates a nested list of BINGO numbers
# e.g. [[1, ..., 15], ... , [61, ..., 75]]
def create_combos():
    #"""Creates list of 75 possible bingo values"""
    combos = []

    # Create 'row' lists with the correct numbers for that row
    # and add them to the combos list.
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []

    for i in range (1, 76):
        if i <= 15:
            row1.append(i)
        elif i <= 30:
            row2.append(i)
        elif i <= 45:
            row3.append(i)
        elif i <= 60:
            row4.append(i)
        else:
            row5.append(i)
            
    combos.append(row1)
    combos.append(row2)
    combos.append(row3)
    combos.append(row4)
    combos.append(row5)

    return combos

# Used in 14.2
# Write a function that prints out a bingo card 
def make_card():
    #"""Creates a bingo card"""
    combos = copy.deepcopy(combinations)        # make a copy of the global variable
    print("-" * 41)
    print("|   B   |   I   |   N   |   G   |   O   |")

    # There are 5 rows in a BINGO card after the header row
    # For each one, get a random number in the correct range for
    # that column. Remove used numbers with .pop() to make sure
    # they are not reused.
    # You'll need to go some work with the spaces and '|' characters.
    for i in range(5):
        print("-" * 41)
        print(("|" + (" " * 7)) * 5 + "|")
        for j in range(5):
        # Add your code here
            print(i, j)  # first make sure you see how this nested for loop
                         # prints out data in a table where i = row, j = column


        print(("|" + (" " * 7)) * 5 + "|")
    print("-" * 41)

# Used in 14.3
# Write a function to calls out a randomly selected Bingo number
# e.g. print out a valid Bingo value, such as B12, N34, 068...
# outputs a bingo number (e.g. "G53"), 
# updated list of combinations (one value shorter),
# and updated list of chosen numbers (one value larger)
def pick_number():
    """Picks a bingo number"""
    letters = ["B", "I", "N", "G", "O"]
    
    # choose a random column by number
    # shuffle the numbers in that column
    
    number = "" # pre-pend the letter to a random number
    
    # add the bingo number to the chosen numbers list
    
    return number  #return the number (for printing)

# 14.1 starts here
# global variables
combinations = []       # This stores all usable numbers
chosen_numbers = []     # This stores all chosen numbers

# main
combinations = create_combos()
print(combinations)
# This will start off only showing [] - fix it by completing the function!


# Uncomment this for 14.2
##need_card = input("\nWould you like to create a bingo card? (Y/N): ")
##if need_card.upper() == "Y":
##   make_card()


# Uncomment this for 14.3
##user_status = input("\nWhen you're ready to play, hit RETURN to start the game: ")
##
##while user_status.upper() != "BINGO!":
##    pick = pick_number()
##    print(pick, "\n")
##    user_status = input("Hit RETURN to choose another number, or type in 'BINGO!': ")

# check if we actually won
##print("\nWE HAVE A WINNER!\nPlease double check:")

# SORT the BINGO numbers we've used and print them HERE
