print("Welcome to the Temperature Conversion APP")
print()
tempFahrenheit = float(input("What is the given temperature in degrees Fahrenheit: "))

tempCelsius = (5/9) * (tempFahrenheit - 32)
tempKelvin = tempCelsius + 273.15

print("Degrees Fahrenheit: " + str(tempFahrenheit))
print("Degrees Celsius: " + str(tempCelsius))
print("Degrees Kelvin: " + str(tempKelvin))