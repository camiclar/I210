# 17.3 Current weather data

# This nested dictionary is from OpenWeather API
# most APIs return something data that looks like this
# (in JavaScript this format is called JSON)
# when you get to I211, you'll learn how to scrape the web and get data from APIs
# in the I399 JavaScript course, you'll work with APIs, maybe even this one
# For I210, we're just going to give you some data as an example to practice with:
# if you want the current weather for IU, you can regrab here:
# https://api.openweathermap.org/data/2.5/weather?zip=47405&appid=bbaf86cac3c0e62ef035b4a051fdf664

data = {
    "coord": {
        "lon": -86.52,
        "lat": 39.17
    },
    "weather": [
        {
            "id": 501,
            "main": "Rain",
            "description": "moderate rain",
            "icon": "10n"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 291.4,
        "feels_like": 292.42,
        "temp_min": 290.93,
        "temp_max": 292.15,
        "pressure": 1014,
        "humidity": 88
    },
    "visibility": 16093,
    "wind": {
        "speed": 1.5,
        "deg": 150
    },
    "rain": {
        "1h": 1.02
    },
    "clouds": {
        "all": 75
    },
    "dt": 1590720375,
    "sys": {
        "type": 1,
        "id": 3471,
        "country": "US",
        "sunrise": 1590661414,
        "sunset": 1590714219
    },
    "timezone": -14400,
    "id": 0,
    "name": "Bloomington",
    "cod": 200
}

# Nested dictionaries like this one are especially useful as data structures
# Investigate the data -- print out the the following:

# (1) Print in a user friendly way -- what are the keys?
print("\nWeather data options:")
for option in data.keys():
    print(option, end=" ")
print()


# (2) Print out the location = "Bloomington"
print("\nLocation:")
print(data["name"])


# (3) Print out the current weather conditions = "moderate rain"
print("\nCurrent conditions:")
print(data["weather"][0]["description"])



# (4) Print the main temperature = "291.4"
# this is in Kelvin - convert to both Fahrenheit and Celsius and label
print("\nCurrent temperature:")
print(data["main"]["temp"])


