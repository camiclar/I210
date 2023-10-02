# 12.1 Pizza order

def order_pizza(size, crust, sauce, topping):
    """Confirms a pizza order"""
    print("One", size, crust, "crust pizza with", sauce, "sauce, topped with", topping + ".")

order_pizza("large", "cauliflower", "pesto", "sun-dried tomatoes")


# (A) To save time for your employees typing in an order, as most customers order 
# a thin crust with red sauce, and only one topping choice, make these the defaults!

# re-write function here
def order_pizza(size, topping, crust="thin", sauce="red"):
    print("One", size, crust, "crust pizza with", sauce, "sauce, topped with", topping + ".")


order_pizza("small", "pepperoni")


# (B) To accommodate the customer who wants a bunch of extra toppings, use *args

# re-write function here

def order_pizza(size, crust="thin", sauce="red", *args):
    print("One", size, crust, "crust pizza with", sauce, "sauce, topped with", end="")
    
    if len(args) > 1:
        for topping in args:
            if args.index(topping) < len(args) - 1:
                print(f" {topping},", end="")
            else:
                print(f" and {topping}.")
    else:
        print(args[0] + ".")


order_pizza("medium", "thick", "red", "pepperoni", "spinach", "mushrooms")


# # Q: Can you use both *args/*kwargs and default parameters?
