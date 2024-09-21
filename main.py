# Function to determine if Rohan can wear light clothes based on temperature
def can_wear_light_clothes(temp):
    if temp >= 20 and temp <= 30:
        return "The temperature is suitable for wearing light clothes!"
    elif temp < 20:
        return "It's too cold! You should wear warm clothes like a jacket or pullover."
    else:
        return "It's too hot! You might get uncomfortable even with light clothes."

# Input: Temperature outside
temperature = float(input("Enter the current temperature (in °C): "))

# Output: Suggestion for Rohan
suggestion = can_wear_light_clothes(temperature)
print(suggestion)
