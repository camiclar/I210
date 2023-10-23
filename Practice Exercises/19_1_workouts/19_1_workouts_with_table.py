# 19.1 Workouts
# Write a program that tallies how many minutes spent on each type of exercise

# import csv module
import csv

# include table_print function
def table_print(headers, data, width=10):
   """prints a nested list in a double column table format"""
   output = "{:<{}} {:<{}}"

   print(output.format(headers[0], width, headers[1], width))

   print("-" * (width + 1) * 2)

   for item1, item2 in sorted(data):
       print(output.format(item1, width, item2, width))
  
   print()


# main
if __name__ == "__main__":
   workout_data = {}
   
   with open("workouts.csv", "r") as csvfile:
      workout_reader = csv.reader(csvfile, delimiter = ",")
      

      for row in workout_reader:
         if row[0] not in workout_data.keys():
            workout_data[row[0]] = int(row[1])
         else:
            workout_data[row[0]] += int(row[1])

   workout_data_list = list(workout_data.items())
   table_print(["Workout Type", "Total Minutes"], workout_data_list, 15)
   
         
# (1) Read in data from workouts.txt
# use csv.reader, which also cleans data for us

# (2) Process the data - use a dictionary to total the minutes

# (3) Print out the results as a table

