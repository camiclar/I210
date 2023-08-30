print("Even or odd?")
num = float(input("Enter a number: "))

if num % 2 == 0:
    print(f"The number {num} is even.")
elif num % 2 == 1:
    print(f"The number {num} is odd.")
else:
    print("That's not a whole number!")
