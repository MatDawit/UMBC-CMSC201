"""
File:    will_it_float.py
Author:  Mathew Dawit
Date:    09/16/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
  Determines if object will float or sink based off density of object.
"""

object_name = input("What object are we putting in the water today? ")
object_weight = float(input("What is the weight of the object? "))
object_volume = float(input("What is the volume of the object? "))
object_density = object_weight/object_volume

if object_density == 1000:
    print(object_name, "has neutral buoyancy.")
elif object_density > 1000:
    print(object_name, "will sink.")
elif object_density < 1000:
    print(object_name, "will float.")
