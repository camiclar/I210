import my_mod
    
# PART 4: Main

#file_path = input("Enter the file path for your data: ") #TODO: Uncomment when done testing
file_path = "spotify_data_2022.csv" # TODO: Delete when done testing

# Issues:
# : or ;
# Empty string

# Error handling for file path
while not my_mod.load_data(file_path):
    file_path = input("\nPlease try again: ")

data = my_mod.load_data(file_path) # Load data

# Menu
print("Welcome to Spotify Data Analysis!\n")

while True:
    # Print out Menu
    print("\tType '1' for audio analysis\n")
    print("\tType '2' for artist info\n")
    print("\tType 'quit' to exit the program\n")

    # Get user input
    answer = input("What would you like to do? ") # TODO: Error handling

    # Allow the user to quit
    if answer.lower() == "quit":
        break

    # Track feature analysis
    elif answer == "1":

        # Track feature
        print("\nTrack features include things like track_danceability, track_loudness, etc.")

        feature = input("What track feature would you like to sort by? ") #TODO: Uncomment when done testing
        #feature = "track_popularity" # TODO: Remove when done testing
        
        # Error handling for track feature
        while feature not in data[0].keys():
            feature = input(f"No feature called {feature}. Please try again: ")

        # Set number of tracks to display
        num_tracks = 0 # TODO: Set to 0 when done testing
        try:
            num_tracks = int(input("How many top tracks would you like to display? ")) #TODO: Uncomment when done testing
            if num_tracks < 1 or num_tracks > len(data): # Makes sure number is in range
                raise ValueError()

        # Exception Handling for Number of Tracks
        except ValueError:
            while True: # Repeats until valid number is entered
                print(f"\nNumber of top tracks must be a digit between 1-{len(data)}.")
                try:
                    num_tracks = int(input("Please try again: "))
                    if num_tracks < 1 or num_tracks > len(data): # If new value is not in range
                        raise ValueError()
                    
                    break
                
                except ValueError:
                    pass

        # Print data
        my_mod.track_analysis(data, feature, num_tracks)    

    # Allow the user to perform an artist info analysis (BONUS)
    elif answer == "2":
        print("\nSorry, this feature isn't implemented yet!")

    # Handle errors as needed!
    else:
        print("Invalid response. Please try again.")
        
    print()

