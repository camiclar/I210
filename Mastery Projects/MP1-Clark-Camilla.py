import random   # Needed for Pt 4

# NOTE FOR GRADERS:
# I'm using classes and functions in this project because I learned
# how to use them in Java from CSCI-C 212 (I recently switched majors from CS to Informatics)
# I looked ahead in Zybooks to lessons 23 and 24 for the Python syntax

class Video:
    
    # Initializes Video object with length, number of views, and watchtime
    def __init__(self, title = "", length = 0.0, views = 0):
        self.title = title
        self.length = length
        self.views = views
        self.watchtime = self.length * float(self.views)

    # Updates watchtime by multiplying video length with number of views
    def update_watchtime(self):
        self.watchtime = self.length * self.views

class Channel:
    
    # Initializes list of videos, number of subscribers, and total watchtime across all videos
    def __init__(self):
        self.videos = [] # Stores Video objects that represent videos on the channel
        self.subscribers = 0
        self.total_watchtime = 0.0

    # PART 1
    
    # Creates Video objects with titles from user input, adds to videos list,
    # repeats until user stops entering titles
    def add_video_titles(self):
        print("\nEnter your videos' titles. Press \"Enter\" when done.")
        while True:
            user_title = input()
            if not user_title: # Checks if user pressed Enter with empty video title
                break
            video = Video(user_title)
            self.videos.append(video)

    # Print all videos entered by the user
    def print_video_titles(self):
        print("\nOkay, here are all of the videos you entered:")
        for video in self.videos:
            print(video.title)

    # PART 2
    
    # Loop through videos list, set lengths for each video from user input
    def set_video_lengths(self):
        print("\nNow we need to add the lengths of each video! Enter the lengths in minutes in this format: 3.5")
        for video in self.videos:
            video.length = float(input(f"How long is \"{video.title}?\" "))

    # Loop through videos list, return index of longest video
    def get_longest_video_index(self):
        max = 0
        for i in range(len(self.videos)):
            if self.videos[i].length > self.videos[max].length:
                max = i
        return max

    # Loop through videos list, return index of shortest video
    def get_shortest_video_index(self):
        min = 0
        for i in range(len(self.videos)):
            if self.videos[i].length < self.videos[min].length:
                min = i
        return min

    # Loop through videos, adding video length to total length,
    # divide total length by number of videos, return result
    def get_avg_length(self):
        total = 0.0
        avg = 0.0
        num_videos = len(self.videos)
        
        for video in self.videos:
            total += video.length

        avg = total / num_videos
        return avg

    # Output shortest, longest, and average video lengths
    def print_video_lengths(self):
        # Call get_shortest_video_index() method, get video at index, assign to shortest_video
        shortest_video = self.videos[self.get_shortest_video_index()]
        longest_video = self.videos[self.get_longest_video_index()]
        avg_length = self.get_avg_length()

        print(f"\nBased on your inputs, your shortest video is \"{shortest_video.title}\" at {shortest_video.length:.1f} minutes")
        print(f"Your longest video is \"{longest_video.title}\" at {longest_video.length:.1f} minutes")
        print(f"Your average video length is {avg_length:.3f} minutes")

    # PART 3
    
    # Sets the number of channel subscribers from user input
    def set_num_subscribers(self):
        self.subscribers = int(input("How many subscribers does your channel have? "))

    # Represents each subscriber watching one random video,
    # video and channel attributes are updated accordingly
    def watch_videos(self):
        for i in range(self.subscribers):
            rand_video_index = random.randrange(len(self.videos)) # Get the index of a random video
            self.videos[rand_video_index].views += 1 # Increment that video's view count

        for video in self.videos:
            video.update_watchtime() # Update watchtime of each video to reflect increased views
            
        self.update_total_watchtime() # Update total watchtime for channel

    # Update channel's total watchtime to reflect video views
    def update_total_watchtime(self):
        self.total_watchtime = 0.0 # Set total_watchtime back to 0.0 in case this method gets called multiple times
        for video in self.videos:
            self.total_watchtime += video.watchtime

    # Output each video's view count, watchtime, and total watchtime
    def print_watchtimes(self):
        print("\nEach subscriber has now watched one video. Here's the breakdown of what they watched:")

        for video in self.videos:
            print(f"{video.title}:")
            print(f"\tViews: {video.views}")
            print(f"\tWatchtime: {video.watchtime:.1f} minutes")
            print()
            
        print(f"Total watchtime across all videos: {self.total_watchtime:.1f} minutes")

    # PART 4

    # Sets number of subscribers to a random number between 1 and 100
    def set_random_subscribers(self):
        self.subscribers = random.randint(1, 100)

    # Populates videos list with random videos
    def create_random_videos(self):
        num_videos = random.randint(3, 10) # Randomly choose how many videos on channel
        for i in range(num_videos):
            length = random.random() * 4 + 1 # Video length is a random float between 1-5
            rand_video = Video("", length) # Title is empty string because it doesn't matter for our purposes
            self.videos.append(rand_video)

# Determines which channel has more watchtime,
# outputs watchtime for each channel and comparison result
def compare_channels(user_channel, competitor_channel):

    # Output the randomized competitor stats, just for fun
    print("Here are some stats about your competitor:")
    competitor_stats = f"Their channel has {competitor_channel.subscribers} subscribers and {len(competitor_channel.videos)} videos,"
    competitor_stats += f" averaging {competitor_channel.get_avg_length():.3f} minutes in length."
    print(competitor_stats)

    # Output total watchtimes
    print(f"\nTheir total watchtime: {competitor_channel.total_watchtime:.3f} minutes")
    print(f"Your total watchtime: {user_channel.total_watchtime:.3f} minutes")
    print()

    # Channel comparison
    if user_channel.total_watchtime > competitor_channel.total_watchtime:
        print("You have more watchtime! Hooray!")
    elif competitor_channel.total_watchtime > user_channel.total_watchtime:
        print("Your competitor has more watchtime! :(")
    else:
        print("It's neck and neck!")

if __name__ == "__main__":
    # PART 1
    print("Let's get started building your video channel!")
    user_channel = Channel() # Create user's channel
    user_channel.add_video_titles() # Creates videos from user titles
    user_channel.print_video_titles()

    # PART 2
    user_channel.set_video_lengths() # Adds user-defined lengths to videos
    user_channel.print_video_lengths()
        
    # PART 3
    print("\nLet's talk about subscribers!")
    user_channel.set_num_subscribers()
    print("\nYour subscribers are watching your videos now...")
    user_channel.watch_videos() # Each subscriber watches a video, updating video and channel attributes in the process
    user_channel.print_watchtimes()


    # PART 4
    print("\nLet's compare our channel to our competitor!")
    competitor_channel = Channel() # Create competitor's channel
    competitor_channel.set_random_subscribers()
    competitor_channel.create_random_videos() # Videos are randomly generated and added to competitor's videos list
    competitor_channel.watch_videos()
    compare_channels(user_channel, competitor_channel) # User and competitor channel watchtimes are compared, results outputted
