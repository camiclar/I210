# 19.2 Bob Ross
# Investigate data about The Joy of Painting

import csv

# lists of data keys by category/topic
structures = ["BARN","BOAT","BRIDGE","BUILDING","CABIN","DOCK","FARM","FENCE","LIGHTHOUSE","MILL","PATH","PERSON","STRUCTURE","WINDMILL"]
vegetation = ["BUSHES","CACTUS","CONIFER","DECIDUOUS","FLOWERS","GRASS","PALM_TREES","TREE","TREES"]
landscapes = ["BEACH","CLIFF","HILLS","LAKE","LAKES","MOUNTAIN","MOUNTAINS","SNOWY_MOUNTAIN","OCEAN","RIVER","ROCKS","WATERFALL","WAVES"]
atmosphere = ["AURORA_BOREALIS","CIRRUS","CLOUDS","CUMULUS","FIRE","FOG","NIGHT","SNOW","SUN","WINTER"]

# (1) Read in the contents of 'bob_ross.csv' using DictReader
# we suggest using a dictionary to count values for each header title
with open("bob_ross.csv", "r", encoding="utf-8-sig") as csvfile:
    bob_ross_reader = csv.DictReader(csvfile)
    header_values = bob_ross_reader.fieldnames
    bob_data = {}
    
    for header in header_values:
        bob_data[header] = 0
        
    for row in bob_ross_reader:
        for header in bob_data.keys():
            if not row[header].isdigit():
                bob_data[header] += 1
            else:
                bob_data[header] += int(row[header])

print(bob_data)
# (2) Use code to investigate the data and answer the following questions:

# Q1: How many episodes of 'The Joy of Painting' aired?

num_episodes = bob_data["EPISODE"]
print(f"'The Joy of Painting' aired {num_episodes} episodes.")


# Q2: Bob would often paint a happy tree.. Who was happy because he had a friend. How many paintings included trees?
num_trees = bob_data["TREE"] + bob_data["TREES"] + bob_data["PALM_TREES"]
print(f"{num_trees} of Bob's paintings included trees")

# Q3: Out of the four categories (vegetation, structures, atmospheric elements or landscape elements), which element did Bob Ross like to paint the most?
max_structure = ""
max_veg = ""
max_landscape = ""
max_atmosphere = ""

for key, value in bob_data.items():
    

# Q4: What did Bob Ross like to paint the most: vegetation, structures, atmospheric elements or landscape elements?

