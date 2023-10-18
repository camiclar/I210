f = open("messy_grocery_list.txt")
contents = f.read()
f.close()

groceries = contents.strip().split(",")
print(groceries)

