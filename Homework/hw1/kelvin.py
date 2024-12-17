"""
File:    kelvin.py
Author:  Mathew Dawit
Date:    09/08/24
Section: 74
E-mail:  mdawit1@umbc.edu
Description:
  Takes number of degrees in Fahrenheit and converts it to Celsius and Kelvin.
"""

temperature_fahrenheit = input("Enter a temperature in Fahrenheit: ")
temperature_celsius = (float(temperature_fahrenheit) - 32) * 5 / 9
temperature_kelvin = temperature_celsius + 273.15

print("The temperature in celsius is", round(temperature_celsius, 2))
print("The temperature in kelvin is", round(temperature_kelvin, 2))
