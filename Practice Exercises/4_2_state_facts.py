# 4.2 State facts
# compares facts about each state

# SET UP
IN_state = {"name": "Indiana",
            "motto": "Crossroads of America",
            "bird": "cardinal",
            "flower": "peony"}
# 1 - create a dictionary for another state
# 2 - add facts about its name, state motto, bird and flower
KY_state = {"name": "Kentucky",
            "motto": "United we stand, divided we fall",
            "bird": "cardinal",
            "flower": "goldenrod"}

# INPUT
# 3 - tell the user what states you will be comparing
# 4 - ask the user for a state fact (assume it is motto, bird or flower)
print(f"Comparing state facts for {IN_state['name']} and {KY_state['name']}:")
fact = input("Which state fact would you like to compare (motto, bird or flower)?:\n")

# PROCESSING / OUTPUT
# 5 - tell the user what the motto, bird or flower is for each state
#   - (this is easier with f strings)
print(f"The {IN_state['name']} state {fact} is {IN_state[fact]}")
print(f"The {KY_state['name']} state {fact} is {KY_state[fact]}")

# 6 - then compare the facts for both states
# 7 - answer the question, are they the same for both states?
print(f"Is the {fact} the same for both? {IN_state[fact] == KY_state[fact]}")
