import csv

# PART 1: Read and clean data

def load_data(file_name):
    # Read in your data (use exception handling)
    try:
        with open(file_name, "r", encoding = "utf-8-sig") as csvfile:
            spotify_reader = csv.DictReader(csvfile)

            # Remove empty rows
            songs = []
            for row in spotify_reader:
                empty_values = [value for value in row.values() if not value] # Checks all values in row; if a value is empty, add to list
                if not empty_values: # If there are no empty values
                    songs.append(row)

        # Remove duplicate entries
        unique_songs = []
        track_names = []
        
        for song in songs:
            if song["track_name"] not in track_names:
                track_names.append(song["track_name"])
                unique_songs.append(song)

        # Convert numerical values to correct data types
        for song in unique_songs:
            for feature, value in song.items():
                try:
                    song[feature] = int(value)
                except ValueError:
                    try:
                        song[feature] = float(value)
                    except ValueError:
                        pass
        
        # Return it!
        return unique_songs

    except FileNotFoundError:
        print(f"Could not find file \"{file_name}\"")
        return []
            
# PART 2: Audio analysis function, sort function, table_print function
# By default, print the 'top 20'
def track_analysis(track_list, feature, cutoff = 20):
    try:
        track_data = []

        # Use track_list to compile the data you need
        for track in track_list:
            
            track_data.append((track["track_name"], track["artist_name"], track[feature]))
        
        # Sort it
        insertion_sort(track_data, 2)
        track_data.reverse()

        # 'Chop off' extra data
        table_data = [track_data[i] for i in range(0, cutoff)]

        # Print it as a table using table_print()
        table_print(["track_name", "artist_name", feature], table_data)

    except KeyError:
        print(f"No feature called {feature}")


# PART 4: BONUS - Artist info function
def artist_info(track_list, artist_name):
    # Populate and display info about the selected artist

    # You can remove this when you start working on this function
    pass

# Implementation of Selection Sort or Insertion Sort for Part 2 and Part 3
def insertion_sort(nested_list, pos):
    # Sort the list
    for i in range(1, len(nested_list)):
        j = i

        while j > 0 and nested_list[j][pos] < nested_list[j - 1][pos]:
            temp = nested_list[j]
            nested_list[j] = nested_list[j - 1]
            nested_list[j - 1] = temp
            j = j - 1

    # Return it
    return nested_list

# Implementation of Table Print for multi-column tables.
# You can have as many header columns as needed.
# Default width for columns is 30.
def table_print(headers, data, width = 30):
    # Modify the one from class to work on 3 columns instead of just 2

    # Print the Headers
    print(f"{headers[0]:<{width}}{headers[1]:<{width}}{headers[2]:<{width}}")
    print("-" * (width * 3))

    # Print the Data
    for item in data:
        print(f"{item[0]:<{width}}{item[1]:<{width}}{item[2]:<{width}}")


# Test code for the Module
if __name__ == "__main__":
    # TEST PART 1
    spotify_data_test = load_data('spotify_data_2022.csv')
    print(len(spotify_data_test), "rows loaded successfully!")
    print()

        
    # TEST PART 2A
    instruments = [("Trumpet", "Brass", 35), ("Saxophone", "Woodwind", 12),
                   ("Snare Drum", "Percussion", 22), ("Cymbal", "Percussion", 40)]
    sorted_instruments = insertion_sort(instruments, 2)
    print(sorted_instruments)
    print()

    # TEST PART 2B
    table_print(["Instrument", "Type", "Amount"], sorted_instruments, 15)
    print()

    # TEST PART 2C
    track_analysis(spotify_data_test, "track_popularity", 10)
    print()
