import random   # Needed for Pt 4

# You are running an online video channel. Your subscribers
# pay to watch videos on your channel of different lengths.
# You also have a competing channel - will your subscribers
# spend more time watching your videos than your competitor's?
# Who will be more successful?!

### Part 1
##print("What are the titles of the videos in your channel?")
##
### Initializing Variables
##videos = {}
##title = " "
##
### User enters video titles into a dictionary that will later hold
### durations for each video. Initialized with 0.0
##print("Enter video titles. Press \"Enter\" when done.")
##while title:
##    title = input()
##    if title: # Prevents empty title from gettting added to dictionary
##        videos[title] = 0.0

# TODO: Delete when done testing
videos = {
    "Welcome to my channel!": 1.5,
    "Here is another video": 9.9,
    "My third video! Woohoo!": 2.3,
    "Yet another super fun video": 4.8,
    "A short video": 0.1,
    "This is a very long video": 57.2
    }

### Looping through dictionary to display all video titles
##print("\nHere are all of the videos you entered:")
##for video in videos:
##    print(video)
##
### Part 2 - How long is each video in your channel?
##print("\nHow long is each video in your channel? Enter length in the format 3.5")
##for video in videos:
##    length = float(input(f"Enter length in minutes for {video}: "))
##    videos[video] = length

print("\nHere are all of your videos and their lengths: ")
for video in videos:
    print(f"{video}: {videos[video]} minutes")

shortest_video = ""
longest_video = ""
total_length = 0.0
avg_length = 0.0

for video in videos:
    if videos[video] < videos[shortest_video]:
        shortest_video = video
    elif videos[video] > videos[longest_video]:
        longest_video = video
    
    total_length += videos[video]

avg_length = total_length / len(videos)

print(f"\nYour shortest video is {shortest_video} at {videos[shortest_video]:.3f} minutes")

# Part 3 - Let's talk about subscribers!
#print("Part 3 - Let's talk about subscribers.")



# Part 4 - Let's compare our channel to our competitor!
#print("Part 4 - Let's compare our channel to our competitor!")

