# 18.2 Save out Bingo Nums

def create_combos():
    """Creates list of 75 possible bingo values"""
    combos = []

    for i in range(1, 75, 15):
        row = []
        for j in range(i, i + 15):
            row.append(j)
        combos.append(row)

    return combos

# main
combinations = create_combos()

# (1) write a list comprehension to change combinations list [[1, 2, ...] ...]
# to a bingo list [["B1", "B2", ...]...]
bingo = ["B", "I", "N", "G", "O"]

bingo_combinations = []

i = 0
while i < len(bingo):
    bingo_combinations.append([])
    
    
    for combination in combinations:
        for number in combination:
            bingo_combinations[i].append(f"{bingo[i]}{number}")
            print(f"{bingo[i]}{number}")
        i += 1

print(bingo_combinations)
# (2) save the output into a file - bingo_nums.txt



print("File saved.")
