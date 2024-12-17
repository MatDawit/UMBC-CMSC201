"""
File:    knobs_and_switches.py
Author:  Mathew Dawit
Date:    09/18/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:    User tries to break into a door using knobs and switches
"""

first_knob = int(input("What is the position of the first knob? (Enter 1-12) "))
second_knob = int(input("What is the position of the second knob? (Enter 1-12) "))
switch_position = input("What is the position of the switch? (Enter up or down) ")

if first_knob < 1 or first_knob > 12:
    print("Knob 1 needs to be set to 1 - 12")

elif second_knob < 1 or second_knob > 12:
    print("Knob 2 needs to be set to 1 - 12")

elif first_knob % 2 != 0 and second_knob % 2 == 0:
    print("The handle doesn't budge.")

elif (first_knob % 2 == 0 or second_knob % 2 != 0) and switch_position == "down":
    print("The door clanks but does not open, try again.")

elif (first_knob % 2 == 0 and second_knob % 2 != 0) and switch_position == "up":
    print("The door opens, you get all the loot.")
