"""
File:    which_month.py
Author:  Mathew Dawit
Date:    09/18/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
    Determines how many months in the future you want to go 
"""

starting_month = int(input("What month are we starting in (enter as an int)? "))
if starting_month < 1 or starting_month > 12:
    print("That is not a month between 1 and 12.")

elif starting_month >= 1 and starting_month <= 12:
    future_month = int(input("How many months in the future should we go? "))

    future_month = future_month % 12
    future_month = starting_month + future_month

    if future_month == 1:
        print("The month will be January")
    elif future_month == 2:
        print("The month will be Feburary")
    elif future_month == 3:
        print("The month will be March")
    elif future_month == 4:
        print("The month will be April")
    elif future_month == 5:
        print("The month will be May")
    elif future_month == 6:
        print("The month will be June")
    elif future_month == 7:
        print("The month will be July")
    elif future_month == 8:
        print("The month will be August")
    elif future_month == 9:
        print("The month will be September")
    elif future_month == 10:
        print("The month will be October")
    elif future_month == 11:
        print("The month will be November")
    elif future_month == 0:
        print("The month will be December")
