FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit
temperature = input("Enter the temperature to convert: ")
if temperature.isnumeric():
    temperature = float(temperature)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
    match unit:
        case 'c':
            converted_temp = convert_to_fahrenheit(temperature)
            print(temperature,"\u2103 is",converted_temp,"\u2109")
        case 'f':
            converted_temp = convert_to_celsius(temperature)
            print(temperature,"\u2109 is",converted_temp,"\u2103")
        case _:
            print("Invalid input. Please enter C or F to indicate which scale is used.")
else:
    print("Invalid temperature. Please enter a numeric value.")
