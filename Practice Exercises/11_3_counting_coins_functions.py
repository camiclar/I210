# 11.3 counting coins using functions
import random

# (1) write a function "create_cup" 
# that takes an integer for how many coins are in the cup
# and returns a list of coins (listed by name)
# e.g. ['dime', 'quarter', ...]

def create_cup(num_coins):
    coin_types = ["penny", "nickel", "dime", "quarter"]
    change = []

    for i in range(num_coins):
        change.append(random.choice(coin_types))

    return change

# (2) write a function "count_coins" 
# that takes in a list of coins,
# counts the coins and returns a dictionary
# results stored as {type: amount}, e.g. {'dime': 16, ...}

def count_coins(coins):
    counted_coins = {}

    for coin in coins:
        if coin not in counted_coins:
            counted_coins[coin] = 1
        else:
            counted_coins[coin] += 1

    return counted_coins

# (3) write a function "print_change" 
# that takes in a dictionary of coins,
# and prints the summary about them.
# There is no need for a return statement!

def print_change(coins):
    quarters = coins["quarter"] * 0.25
    dimes = coins["dime"] * 0.10
    nickels = coins["nickel"] * 0.05
    pennies = coins["penny"] * 0.01

    total = quarters + dimes + nickels + pennies

    print('Quarters: ${:.2f}'.format(quarters))
    print('Dimes: ${:.2f}'.format(dimes))
    print('Nickels: ${:.2f}'.format(nickels))
    print('Pennies: ${:.2f}'.format(pennies))

    print('\nTotal change in cup: ${:.2f}'.format(total))
    

# SET-UP
# main

if __name__ == "__main__":
    num_coins = int(input("Input how many coins are in the cup: "))
    print()

    cup = create_cup(num_coins)
    counted_coins = count_coins(cup)
    print_change(counted_coins)
