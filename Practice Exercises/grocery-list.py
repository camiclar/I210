groceries = []

user_item = input("Add an item to the grocery list: ")

while user_item:
    groceries.append(user_item)
    user_item = input("Add an item to the grocery list: ")

print(f"Your grocery list has {len(groceries)} items:")
print(groceries)
