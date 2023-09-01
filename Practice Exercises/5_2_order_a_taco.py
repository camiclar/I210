# 5.2 Order a taco 

# SET UP
veggies = ["chili-fried tofu", "spicy tempeh", "refried beans"]
meats = ["ground beef", "pork carnitas", "spicy chicken"]
toppings = ["radishes", "pickled onion", "cilantro"]

print("Place your taco order:")

# INPUT / PROCESSING
# choose a tortilla
tortilla = input("Would you like a corn or flour torilla? ")

# vegetarian?
vegetarian = input("Are you a vegetarian? (Y / N): ")
if vegetarian == "N":
    i = 1
    for meat in meats:
        print(f"Choose {i} for {meat}")
        i += 1
    protein_choice = int(input("\nWhich protein would you like? ")) - 1
    protein = meats[protein_choice]
else:
    i = 1
    for veggie in veggies:
        print(f"Choose {i} for {veggie}")
        i += 1
    protein_choice = int(input("\nWhich protein would you like? ")) - 1

  
# choose a topping
print("\nNow choose a topping:")
i = 1
for topping in toppings:
    print(f"Choose {i} for {topping}")
    i += 1

topping_choice = int(input("\nWhich would you like? ")) - 1
vegetable = toppings[topping_choice]

# salsa?
salsa = input("\nWould you like spicy salsa on that? (Y / N): ")

# OUTPUT
# display taco order
order = "Okay, that's one"
if protein:
    order += " " + protein
order += f" taco on a {tortilla} tortilla with {vegetable}"

if salsa == "Y":
    order += ", and our spicy salsa."
else:
    order += "."

print(order)





