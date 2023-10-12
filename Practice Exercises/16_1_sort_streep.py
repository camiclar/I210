# 16.1 Sort Streep on Screen and Stage
# Sort this list of Meryl Streep's performances

performances = [["The Devil Wears Prada", "Drama", 2006], ["It's Complicated", "Comedy", 2009],
                ["Hope Springs", "Comedy", 2012], ["The Bridges of Madison County", "Drama", 1995],
                ["Out of Africa", "Drama", 1985], ["Little Women", "Drama", 2019],
                ["Mamma Mia!", "Musical", 2008], ["Fantastic Mr Fox", "Animated", 2009],
                ["The Taming of the Shrew", "Comedy", 1978], ["Julia", "Drama", 1977],
                ["Silkwood", "Drama", 1983], ["Florence Foster Jenkins", "Drama", 2016],
                ["Henry V", "Drama", 1976], ["The Iron Lady", "Drama", 2011],
                ["Julia & Julia", "Drama", 2009], ["The French Lieutenant's Woman", "Drama", 1981],
                ["The Seagull", "Drama", 2004], ["Into the Woods", "Musical", 2014],
                ["Big Little Lies", "Drama", 2019], ["The Post", "Drama", 2017]]

print("UNSORTED: ")
print(performances)

# use a standard sort to sort the list by title
performances.sort()

print("\nSORTED by title: ")
print(performances)

# use selection sort or insertion sort to sort the list by date
# you can still use the inequality operators (<, >, <=, >=) on strings,
# and this will allow you to sort strings into alphabetic order
for i in range(1, len(performances)):
    j = i
    while j > 0 and performances[j][-1] < performances[j - 1][-1]:
        temp = performances[j]
        performances[j] = performances[j - 1]
        performances[j - 1] = temp
        j = j - 1



print("\nSORTED by date: ")
print(performances)


