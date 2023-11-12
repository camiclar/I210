import my_mod
    
# PART 4: Main

# Load Data
file_path = input("Enter the file path for your data: ")
data = []

try:
    data = my_mod.load_data(file_path)
    
    if not data: # load_data returns an empty list if an error occurs. This makes sure the empty list doesn't cause issues
        raise Exception
except Exception:
    while not data: # Loops until the user enters a valid file path that returns data
        file_path = input("\nCouldn't locate data. Please try again with a different file path: ")

        try:
            data = my_mod.load_data(file_path)
        except:
            pass

# Menu
print("Welcome to Spotify Data Analysis!\n")

while True:
    # Print out Menu
    print("\tType '1' for audio analysis\n")
    print("\tType '2' for artist info\n")
    print("\tType 'quit' to exit the program\n")

    # Get user input for menu choice
    answer = input("What would you like to do? ")

    # Allow the user to quit
    if answer.lower() == "quit":
        break

    # Track feature analysis
    elif answer == "1":

        # Track feature
        print("\nTrack features include things like track_danceability, track_loudness, etc.")

        feature = input("What track feature would you like to sort by? ")
        
        # Error handling for track feature
        while feature not in data[0].keys():
            feature = input(f"No feature called {feature}. Please try again: ")

        # Set number of tracks to display
        num_tracks = 0
        try:
            num_tracks = int(input("How many top tracks would you like to display? "))
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
        print()
        my_mod.track_analysis(data, feature, num_tracks)    

    # Allow the user to perform an artist info analysis (BONUS)
    elif answer == "2":
        print("\nSorry, this feature isn't implemented yet!")

    # Handle errors as needed!
    else:
        print("Invalid response. Please try again.")
        
    print()

