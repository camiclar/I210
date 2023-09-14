# 9.1 Counting coins
import random  # you'll need random for this exercise

# SET-UP
types_of_coins = ["penny", "nickel", "dime", "quarter"]
change = []
counted_coins = {}
coin_values = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25
    }

# CREATE A CUP FULL OF CHANGE (create the input)
# randomly create a list of coins to represent your PizzaX cup full of change

for i in range(50):
    change.append(random.choice(types_of_coins))

print(change)

# COUNT HOW MANY COINS OF EACH TYPE (process the data)
counted_coins["penny"] = 0
counted_coins["nickel"] = 0
counted_coins["dime"] = 0
counted_coins["quarter"] = 0

for coin in change:
    counted_coins[coin] += 1

print(counted_coins)



# (3) CALCULATE THE MONETARY VALUE (calculate and output)
# use code to answer these questions
penny_total = 0.0
nickel_total = 0.0
dime_total = 0.0
quarter_total = 0.0

for coin in counted_coins:
    if coin == "penny":
        penny_total += counted_coins[coin] * coin_values[coin]
    elif coin == "nickel":
        nickel_total += counted_coins[coin] * coin_values[coin]
    elif coin == "dime":
        dime_total += counted_coins[coin] * coin_values[coin]
    elif coin == "quarter":
        quarter_total += counted_coins[coin] * coin_values[coin]

total = penny_total + nickel_total + dime_total + quarter_total

# Q: What is the monetary value of each type of coin?
# e.g. if I have 3 dimes, I have $0.30 in dimes
print(f"Quarters: ${quarter_total:.2f}")
print(f"Dimes: ${dime_total:.2f}")
print(f"Nickels: ${nickel_total:.2f}")
print(f"Pennies: ${penny_total:.2f}")
print(f"Total: ${total:.2f}")



# Q: What is the total amount of money in the change cup?





