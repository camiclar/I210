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
                    songs.append(row["track_name"])

        # Remove duplicate entries
        unique_songs = []
        
        for song in songs:
            if song not in unique_songs:
                unique_songs.append(song)

        # Return it!
        return unique_songs

    except FileNotFoundError:
        print(f"Could not find file {file_name}")
        return []
            
# PART 2: Audio analysis function, sort function, table_print function
# By default, print the 'top 20'
def track_analysis(track_list, feature, cutoff = 20):
    # Use track_list to compile the data you need

    # Sort it

    # 'Chop off' extra data

    # Print it as a table using table_print()

    # You can remove this when you start working on this function
    pass

# PART 4: BONUS - Artist info function
def artist_info(track_list, artist_name):
    # Populate and display info about the selected artist

    # You can remove this when you start working on this function
    pass

# Implementation of Selection Sort or Insertion Sort for Part 2 and Part 3
def your_sort(nested_list, pos):
    # Modify the one from class to work on column pos (position)

    # Sort the list

    # Return it
    
    # You can remove this when you start working on this function
    pass

# Implementation of Table Print for multi-column tables.
# You can have as many header columns as needed.
# Default width for columns is 30.
def table_print(headers, data, width = 30):
    # Modify the one from class to work on 3 columns instead of just 2

    # Print the Headers

    # Print the Data

    # You can remove this when you start working on this function
    pass


# Test code for the Module
if __name__ == "__main__":
    # TEST PART 1
    spotify_data_test = load_data('spotify_data_2022.csv')
    print(len(spotify_data_test), "rows loaded successfully!")
    print()

        
    # TEST PART 2A
    instruments = [("Trumpet", "Brass", 35), ("Saxophone", "Woodwind", 12),
                   ("Snare Drum", "Percussion", 22), ("Cymbal", "Percussion", 40)]
    sorted_instruments = your_sort(instruments, 2)
    print(sorted_instruments)
    print()

    # TEST PART 2B
    table_print(["Instrument", "Type", "Amount"], sorted_instruments, 15)
    print()

    # TEST PART 2C
    track_analysis(spotify_data_test, "track_popularity", 10)
    print()
