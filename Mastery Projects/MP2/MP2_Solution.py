import my_mod

    
# PART 4: Main

# Use your module to load the data from spotify_data_2022.csv
# HERE
print("Welcome to Spotify Data Analysis!\n")
#file_path = input("Enter the file path for your data: ") #TODO: Uncomment when done testing
file_path = "spotify_data_2022.csv"

while not my_mod.load_data(file_path):
    file_path = input("\nPlease try again: ")

data = my_mod.load_data(file_path)

while True:
    # Print our Menu
    print("\n\tType '1' for audio analysis\n")
    print("\tType '2' for artist info\n")
    print("\tType 'quit' to exit the program\n")

    # Get user input
    answer = input("What would you like to do? ")

    # Allow the user to quit
    if answer.lower() == "quit":
        break

    # Allow the user to perform a track feature analysis
    elif answer == "1":
        print("\nTrack features include things like track_danceability, track_loudness, etc.")
        #user_feature = input("What track feature would you like to sort by? ")

        num_tracks = 15 # TODO: Set to 0 when done testing
        try:
            #num_tracks = int(input("How many top tracks would you like to display? ")) #TODO: Uncomment when done testing
            if num_tracks < 1 or num_tracks > len(data): # Makes sure number is in range
                raise ValueError()
            
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


    # Allow the user to perform an artist info analysis (BONUS)

    # Handle errors as needed!
        
    print()
                                 
