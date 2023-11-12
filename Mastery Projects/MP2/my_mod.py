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
        unique_songs = [] # Contains dictionaries that represent songs
        track_names = [] # Contains song names as strings. Keeps track of which songs have been added to unique_songs
        
        for song in songs:
            if song["track_name"] not in track_names: # If song's name hasn't been added to track_names
                track_names.append(song["track_name"]) # Add song's name to track_names
                unique_songs.append(song) # Add song dictionary to unique_songs

        # Convert numerical values to correct data types (int or float)
        for song in unique_songs:
            for feature, value in song.items(): # Loop through each value and feature in each song
                try:
                    song[feature] = int(value) # Try converting value to int
                except ValueError:
                    try:
                        song[feature] = float(value) # Try converting value to float
                    except ValueError:
                        pass # Leave value as string
        
        # Return it!
        return unique_songs

    except FileNotFoundError: # Returns empty list if invalid file path
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
        table_print(["track_name", "artist_name", feature], table_data, 22)

    except KeyError:
        print(f"No feature called \"{feature}\"")


# PART 4: BONUS - Artist info function
def artist_info(track_list, artist_name):
    # Populate and display info about the selected artist

    # Variables
    artist_in_data = False
    num_followers = 0
    popularity = 0
    tracks = []
    genres = []

    artist_total_energy = 0.0
    artist_total_valence = 0.0
    all_total_energy = 0.0
    all_total_valence = 0.0


    # Process initial data
    for track in track_list:
        all_total_energy += track["track_energy"]
        all_total_valence += track["track_valence"]
        
        if track["artist_name"] == artist_name:
            artist_in_data = True # Checking to see if artist_name is valid
            num_followers = track["artist_followers"] # Number of followers
            popularity = track["artist_popularity"] # Popularity score
            
            genres = track["artist_genres"].split(",") # Genres
            for i in range(len(genres)):
                genres[i] = genres[i].strip()

            tracks.append(track) # Tracks

            # Energy and valence
            artist_total_energy += track["track_energy"]
            artist_total_valence += track["track_valence"]

    if not artist_in_data:
        print(f"Couldn't find artist \"{artist_name}.\"\n")

    else:
        # Header
        header = f"{artist_name}'s Spotify Snapshot"
        print(header)
        print("-" * len(header))

        # Number of Followers
        print(f"# Followers: {num_followers}")

        # Popularity score
        print(f"Popularity score: {popularity}")

        # Genres
        print("Genres: ", end="")
        for i in range(len(genres)):
            if i < len(genres) - 1:
                print(genres[i], end=", ")
            else:
                print(genres[i])

        # Tracks
        print("\nTracks released:")

        for track in tracks:
            name = "track_name"
            print(f"\t'{track[name]}'")
        print()

        # Most popular song
        track_popularity_data = []
        for track in tracks: # Create list of tuples for insertion sort
            track_popularity_data.append((track["track_name"], track["track_popularity"]))
        insertion_sort(track_popularity_data, 1) # Sort songs based on popularity
        track_popularity_data.reverse()

        print(f"Most popular song: {track_popularity_data[0][0]}\n") # Print song at top of popularity list

        # Energy and valence ratings
        artist_avg_energy = artist_total_energy / len(tracks) # Calculate artist's average
        artist_avg_valence = artist_total_valence / len(tracks)

        all_avg_energy = all_total_energy / len(track_list) # Calculate average across all tracks
        all_avg_valence = all_total_valence / len(track_list)
        
        # Print results
        print(f"With an energy score of {artist_avg_energy:.3f}, {artist_name}'s music is ", end="")
        if artist_avg_energy > all_avg_energy:
            print("more energetic than average.")
        elif artist_avg_energy < all_avg_energy:
            print("less energetic than average.")
        else:
            print("equal to the average.")
        
        print(f"With a valence score of {artist_avg_valence:.3f}, {artist_name}'s music is ", end="")
        if artist_avg_valence > all_avg_valence:
            print("happier than average.")
        elif artist_avg_valence < all_avg_valence:
            print("more sad than average.")
        else:
            print("equal to the average.")
            
        print()

# Implementation of Insertion Sort for Part 2 and Part 3
def insertion_sort(nested_list, pos):
    # Sort the list

    # Sorting by feature
    # Mostly taken from Zybooks Figure 16.7.1
    for i in range(1, len(nested_list)):
        j = i

        while j > 0 and nested_list[j][pos] < nested_list[j - 1][pos]:
            temp = nested_list[j]
            nested_list[j] = nested_list[j - 1]
            nested_list[j - 1] = temp
            j = j - 1

    # Sorts items with equal features alphabetically by track_name
    for i in range(1, len(nested_list)):
        j = i

        while j > 0 and str(nested_list[j][0]) > str(nested_list[j - 1][0]) and nested_list[j][pos] == nested_list[j - 1][pos]:
            temp = nested_list[j]
            nested_list[j] = nested_list[j - 1]
            nested_list[j - 1] = temp
            j = j - 1
    
    # Return it
    return nested_list

# Implementation of Table Print for multi-column tables.
def table_print(headers, data, width = 30):
    # Prints data dynamically based on number of columns provided (could print more than 3 columns if needed)
    # and length of data values (adds more width if one value is very long)

    column_widths = [0 for i in range(len(headers))] # Initialize list that stores column widths
    for item in data:
        for i in range(len(item)):
            if len(str(item[i])) > column_widths[i]: # Sets each column's width to the length of the longest value
                column_widths[i] = len(str(item[i]))

    total_width = 0 # Initialize total table width (for dashed line)
    for i in range(len(column_widths)):
        padding = 3 # Amount of space between columns
    
        if column_widths[i] + padding < width:
            column_widths[i] = width # If no values longer than default width, keep default width
        else:
            column_widths[i] += padding # If value is longer than default width, use that + padding

        total_width += column_widths[i]

    # Print headers
    for i in range(len(headers)):
        print(f"{headers[i]:<{column_widths[i]}}", end="")
    print()

    # Print dashed line
    print("-" * total_width)

    # Print values
    for item in data:
        for i in range(len(item)):
            print(f"{item[i]:<{column_widths[i]}}", end="")
        print()


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

    # TEST PART 4
    artist_info(spotify_data_test, "Kendrick Lamar")
