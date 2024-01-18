import random

cities = ["Kyiv", "Kharkiv", "Odesa", "Dnipro", "Lviv"]
conditions = ["Sunny", "Cloudy", "Rainy", "Snowy"]
temp_ranges = {
    "Sunny": (18, 25),
    "Cloudy": (8, 15),
    "Rainy": (7, 17),
    "Snowy": (-15, -5),
}
wind_ranges = {
    "Sunny": (2, 7),
    "Cloudy": (5, 9),
    "Rainy": (7, 12),
    "Snowy": (10, 15),
}

print("Please choose one of the following Ukrainian cities:")
for i, city in enumerate(cities, start=1):
    print(f"{i}. {city}")

while True:
    try:
        choice = int(input("Enter the number of your chosen city: "))
        if 1 <= choice <= len(cities):
            break
        else:
            print("Invalid choice. Please enter a number between 1 and", len(cities))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and", len(cities))

chosen_city = cities[choice - 1]

print("-------------------------------------------------------")

forecasts = ["Hourly forecast", "Daily forecast", "3-day forecast"]

print("Choose weather forecast:")
for i, forecast in enumerate(forecasts, start=1):
    print(f"{i}. {forecast}")

while True:
    try:
        choice2 = int(input("Enter the number of your chosen forecast: "))
        if 1 <= choice2 <= len(forecasts):
            break
        else:
            print("Invalid choice. Please enter a number between 1 and", len(forecasts))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and", len(forecasts))

chosen_forecast = forecasts[choice2 - 1]

print("-------------------------------------------------------")


def generate_weather_with_disaster():
    while True:
        if random.randint(0, 100) <= 7:
            weather = {
                'temperature': random.uniform(-25, -16),
                'wind_speed': random.uniform(20, 30),
                'condition': "Blizzard (disaster)",
            }
        else:
            condition = random.choice(conditions)
            temperature_dinamic = random.uniform(temp_ranges[condition][0], temp_ranges[condition][1])
            wind_speed_dinamic = random.uniform(wind_ranges[condition][0], wind_ranges[condition][1])
            weather = {
                'temperature': temperature_dinamic,
                'wind_speed': wind_speed_dinamic,
                'condition': condition
            }
        yield weather


def generate_weather():
        while True:
            condition = random.choice(conditions)
            temperature_dinamic = random.uniform(temp_ranges[condition][0], temp_ranges[condition][1])
            wind_speed_dinamic = random.uniform(wind_ranges[condition][0], wind_ranges[condition][1])
            weather = {
                    'temperature': temperature_dinamic,
                    'wind_speed': wind_speed_dinamic,
                    'condition': condition
                }
            yield weather
        


weather_generator = generate_weather()
weather_generator2 = generate_weather_with_disaster()

def display_weather_conditions_hourly():
    print(f"City: {chosen_city}")
    for _ in range(12, 25):
        print(f" {_} -  hour")
        weather = next(weather_generator)
        print(f"Temperature: {weather['temperature']:.2f}°C")
        print(f"Wind Speed: {weather['wind_speed']:.2f} km/h")
        print(f"Condition: {weather['condition']}")
        print("\n")


def display_weather_conditions_daily():
    print(f"City: {chosen_city}")
    for _ in range(1, 15):
        print(f" {_} -  day")
        weather = next(weather_generator2)
        print(f"Temperature: {weather['temperature']:.2f}°C")
        print(f"Wind Speed: {weather['wind_speed']:.2f} km/h")
        print(f"Condition: {weather['condition']}")
        print("\n")



def display_weather_conditions_3_day():
    print(f"City: {chosen_city}")
    for _ in range(1, 8):
        print(f" {_}  -  3 day")
        weather = next(weather_generator2)
        print(f"Temperature: {weather['temperature']:.2f}°C")
        print(f"Wind Speed: {weather['wind_speed']:.2f} km/h")
        print(f"Condition: {weather['condition']}")
        print("\n")


if chosen_forecast == "Hourly forecast":
    display_weather_conditions_hourly()

if chosen_forecast == "Daily forecast":
    display_weather_conditions_daily()

if chosen_forecast == "3-day forecast":
    display_weather_conditions_3_day()
