"""
File:    escape_velocity.py
Author:  Mathew Dawit
Date:    09/08/24
Section: 74
E-mail:  mdawit1@umbc.edu
Description:
  Program which calculates the velocity required to escape the gravitation pull of an object.
"""

launch_body = input("What body are we launching from? ")
launch_body_mass_coefficient = float(input("Enter the mass of the planet in scientific notation with the floating number first: "))
launch_body_mass_power_of_ten = int(input("What power of 10 is this? "))
radius_from_launch_body = float(input("Enter the coefficient of the scientific notation of the radius from the center of Earth: "))
radius_power_of_ten = int(input("What power of 10 is this? "))

escape_velocity = ((2 * (6.67 * 10 ** (-11)) * (launch_body_mass_coefficient * 10 ** launch_body_mass_power_of_ten)) / (radius_from_launch_body * 10**radius_power_of_ten)) ** 0.5

print("The escape velocity required for", launch_body, "is", round(escape_velocity, 3), "m/s")
