# 8.3 Order a taco (updated)
# refactor to use loops

# SET UP
veggies = ["chili-fried tofu", "spicy tempeh", "refried beans"]
meats = ["ground beef", "pork carnitas", "spicy chicken"]
toppings = ["radishes", "pickled onion", "cilantro"]

print("\nPlace your taco order:")

# INPUT / PROCESSING
# choose a tortilla
tortilla = input("Would you like a corn or flour tortilla? ")

# vegetarian?
is_veg = input("\nAre you vegetarian? (Y / N): ")

# choose a protein
if is_veg == "Y":
    proteins = veggies
else:
    proteins = meats
    
print("\tChoose 1 for", proteins[0])
print("\tChoose 2 for", proteins[1])
print("\tChoose 3 for", proteins[2])

choice = input("\nWhich protein would you like? ")

protein = proteins[int(choice) - 1]
  
# choose a topping
print("\n Now choose a topping:")

print("\tChoose 1 for", toppings[0])
print("\tChoose 2 for", toppings[1])
print("\tChoose 3 for", toppings[2])

top_choice = input("\nWhich topping would you like? ")

topping = toppings[int(top_choice) - 1]

# salsa?
salsa_choice = input("\nWould you like spicy salsa on that? (Y / N): ")
if salsa_choice == "Y":
    salsa = "and our spicy salsa"
else:
    salsa = "hold the salsa"

# OUTPUT
# display taco order
taco_order = "\nOk, that's one {} taco on a {} tortilla with {}, {}."
print(taco_order.format(protein, tortilla, topping, salsa))





