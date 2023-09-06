# 6.2 Weather app (version 1)
# a tries really hard to be helpful app where YOU enter all the information!

# SETUP - Welcome the user to Weather App 1.0
print("Welcome to Weather App 1.0!")

# (1) Weather app converts your temperature!
# INPUT - ask the user some weather related questions
# Q1: Please enter your current temperature:
user_temp = float(input("Please enter your current temperature: "))

# Q2: Is this temperature in Fahrenheit or Celsius? Enter F or C:
temp_choice = input("Is this temperature in Fahrenheit or Celsius? Enter F or C: ")

# PROCESSING / OUTPUT - helpfully calculate the temperature in F or C
# temperatures should be displayed to one decimal position

f_temp = 0
c_temp = 0
if temp_choice == "F":
    f_temp = user_temp
    c_temp = (5 / 9) * (f_temp - 32.0)
elif temp_choice == "C":
    c_temp = user_temp
    f_temp = (c_temp * (9 / 5) + 32)

print(f"Your current temperature is {f_temp:.1f}F / {c_temp:.1f}C\n")

# Figure out if the temperature is "hot" (75 or higher F) or "cold" (40 or lower F)
temp_description = ""
if f_temp >= 75:
    temp_description = "hot"
elif f_temp <= 40:
    temp_description = "cold"
else:
    temp_description = "temperate"


# (2) Weather app tells you what to wear!
# Let's figure out what you should wear to be prepared for the weather...
print("Let's figure our what you should wear to be prepared for the weather...")

# SETUP
# Print a message to explain we're asking about current weather conditions.
print("What are your weather conditions?")

# INPUT - ask user about current conditions
# What are your current weather conditions?
# Q3: Enter sunny, raining, or neither:
conditions = input("Enter sunny, raining, or neither: ")

# PROCESSING - create custom advice on user's fashion choices
    # raining and hot
    # raining and cold
    # raining and neither
    # sunny and hot
    # sunny and cold
    # sunny and neither
    # hot
    # cold
    # neither - advise the user to wear layers

conditions_advice = {
    "raining": "Bring an umbrella.",
    "sunny": "Put on sunglasses.",
    "neither": "Wear something fun!"
    }
temp_advice = {
    "hot": "Wear a t-shirt.",
    "cold": "Wear a jacket.",
    "temperate": "Wear layers."
    }

# OUTPUT - print out the message
print("Our advice is:")
print(f"--{conditions_advice[conditions]}")
print(f"--{temp_advice[temp_description]}")

