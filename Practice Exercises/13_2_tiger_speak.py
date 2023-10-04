# 13.2 Tiger speak
import random

# Write a function "tiger_speak":
# (takes a string, returns a string)
# Rules for tiger speak:
# Each character is **randomly** upper or lower case
# Every space is now a dash - tigers have stripes!

def tiger_speak(sentence):
    output_sentence = ""

    for i in range(len(sentence)):
        is_upper = random.randint(0, 1)
        if is_upper:
            output_sentence += sentence[i].upper()
        else:
            output_sentence += sentence[i].lower()

    output_sentence = output_sentence.replace(" ", "-")

    return output_sentence




# main
if __name__ == "__main__":
    sentence1 = "Tyger Tyger, burning bright,"
    sentence2 = "In the forests of the night,"
    sentence3 = "What immortal hand or eye,"
    sentence4 = "Could frame thy fearful symmetry?"

    print(tiger_speak(sentence1))
    print(tiger_speak(sentence2))
    print(tiger_speak(sentence3))
    print(tiger_speak(sentence4))



# Make your sentences wild like a tiger:
# Get four sentences from the user and put them in a list
# Write a function that takes a sentence
# and returns a sentence with a tiger twist
# Walk through and print out the sentences






# example output:
# Tyger Tyger, burning bright,
# In the forests of the night,
# What immortal hand or eye,
# Could frame thy fearful symmetry?

# TygEr-TYger,-buRNing-bRigHT,
# in-THE-fOrestS-Of-tHe-NIGhT,
# wHAT-ImmorTaL-hANd-OR-Eye,
# CoULD-FrAme-THY-FEARFul-syMmeTrY?

