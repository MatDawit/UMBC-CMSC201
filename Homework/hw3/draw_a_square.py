"""
File:    draw_a_square.py
Author:  Mathew Dawit
Date:    09/22/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description: Progam draws a square using stars from user input
"""

vertical_rows = int(input("How many rows (vertical) do you want? "))
horizontal_rows = int(input("How many rows (horizontal) do you want?"))

for i in range(horizontal_rows):
    print("*", end="")
print()

for i in range(vertical_rows-2):
    print("*", end="")
    for j in range(horizontal_rows-2):
        print(" ", end="")
    print("*")

for i in range(horizontal_rows):
    print("*", end="")
print()
