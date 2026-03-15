# Take input in Celsius and print its equivalent in Fahrenheit and kelvin.

Celsius = float(input("Enter temperature in Celsius :"))

Fahrenheit = (Celsius * 9/5) + 32
Kelvin = Celsius + 273.15

print("Celsius --> Fahrenheit =", Fahrenheit )
print("Celsius --> Kelvin =", Kelvin)