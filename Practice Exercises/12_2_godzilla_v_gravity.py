# 12.2 Godzilla v Gravity
# tip: you'll need the math module for this to find the square root
import math

# functions
# write a function drop_time that takes two heights and returns two times in seconds
# time = how long it takes to fall from the ground from a set height
# t = √(2h/g)

def drop_time(height1, height2):
    time1 = math.sqrt((height1 * 2) / gravity)
    time2 = math.sqrt((height2 * 2) / gravity)
    return [time1, time2]

# globals
# set a constant for acceleration due to gravity 
# on earth, gravity is 9.8 meters per second squared
gravity = 9.8

# main
print("Compare the height of two tall objects: ")
print("How long it will take for an object to fall to the ground from the heads of these Godzillas?")

# GODZILLA DATA:
# Godzilla 2019                 119.8m
# Godzilla 2004                 100m
# Showa Mechagodzilla 1974      50m
# Toho Godzilla 1954            50m

# get the input as two lists (one per input) with information about each kaiju
# since we are expecting complex input for this problem that is difficult
# to enter through an input(), please use eval()
# example input1: ['Toho Godzilla 1954', 50]
# example input2: ['Godzilla 2019', 119.8]


# use the function drop_time to calculate how long it takes 
# to drop an object from the top of two different kaiju


# output the results



# Need help writing the equation? 
# Here's an example.. plug in 200m to check that you've got it right (6.39s)
# How long does it take for an object to fall 200 meters? 
# (g = 9.8m/s2, h = height, s = seconds)
#     t = √(2h/g)
#     t = √[2*(200 m)/(9.8 m/s2)]
#     t = √(40.8 s2)
#     t = 6.39 s
