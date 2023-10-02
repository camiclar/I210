# 13.1 JOIN THE EXCITEMENT WARS

# HELLO EVERYONE!!! THIS EXERCISE IS GOING TO BE EPIC!!! WRITE A PROGRAM THAT
# MAKES ALL OF YOUR SENTENCES SOUND LIKE YOU'RE A FAMOUS YOUTUBER!!!
# ABOUT WHY YOUTUBERS LIKE TO BE LOUD: https://youtu.be/Du20dCX_6xs


# FUNCTION: write a function "excited_speak" that takes a message and returns it all worked up
# Rules for exciting speak:
# if sentence ends in . or no punctuation -- it should now end in !!!
# if sentence ends in ! -- it should still just end in !!!
# if sentence ends in ? -- it should end in ???
# CAPITALIZE ALL LETTERS!

def excited_speak(message):
    message = message.upper()

    characters_to_replace = [".", "!", "?"]
    for character in characters_to_replace:
        if message.endswith(character):
            if character != "?":
                message = message.replace(character, "!!!")
            else:
                message = message.replace(character, "???")
    
    return message


# FUNCTION: write a function "calm_speak" that takes a message and returns it all calmed down
# Rules for calm speak:
# take off any triple punctuation at the end
# if it's a ??? -- should now end in a ?
# otherwise it should end in a .
# follow standard punctuation rules

def calm_speak(message):
    message = message.capitalize()
    if message.endswith("!!!"):
        message = message.replace("!!!", ".")
    elif message.endswith("???"):
        message = message.replace("???", "?")

    return message

# main
# INPUT: get a message from the user

if __name__ == "__main__":
    #user_message = input("TYPE YOUR TOTALLY LAME MESSAGE HERE AND WE'LL MAKE IT EPIC!!!\n")

# PROCESSING & OUTPUT: convert the message to excited speak and print the result
    #print(excited_speak(user_message))
    #print(excited_speak("Hello? Is anyone there!"))


# PROCESSING & OUTPUT: convert the message to calm speak and print the result
    print(calm_speak("THIS MESSAGE IS TOTALLY EPIC???"))

