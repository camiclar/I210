## 3.3 Movie night

# Meet the dad. He owns several favorite movies. Some he likes so much he has multiple copies.
dad_movies = ["Die Hard", "Jaws", "Alien", "Princess Mononoke", "Die Hard", "Alien", "Jurassic World"]

# Meet the kid. He also owns some favorite movies.
kid_movies = ["Jurassic World", "Princess Mononoke", "Dragonball Z", "Kung Fu Panda", "How to Train Your Dragon"]

#1 Make each movie list only contain one copy of each movie by transforming them into sets
dad_set = set(dad_movies)
kid_set = set(kid_movies)
print(f"The dad likes: {dad_set}")
print(f"The kid likes: {kid_set}")

#2 What movies do the dad and kid have to select from? (List all movies in either list)
print(f"All movie choices: {dad_set.union(kid_set)}")

#3 What movies are liked by either the dad or the kid, but not both?
print(f"Movies only one of them likes: {dad_set.symmetric_difference(kid_set)}")

#4 What movies does only the dad like?
print(f"Movies only the dad likes: {dad_set.difference(kid_set)}")


#5 What movies do both the dad and the kid like?
print(f"Movies the dad and kid can agree on: {dad_set.intersection(kid_set)}")

# (Still have two choices for movie night! Hope they can agree on one. ;-)
