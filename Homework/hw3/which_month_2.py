"""
File:    which_month_2.py
Author:  Mathew Dawit
Date:    09/22/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description: Determines how many months in the future you want to go 
"""

starting_month = int(input("What month are we starting in (enter as an int)? "))
list_of_months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if starting_month < 1 or starting_month > 12:
    print("That is not a month between 1 and 12.")

elif starting_month >= 1 and starting_month <= 12:
    future_month = int(input("How many months in the future should we go? "))

    future_month = future_month % 12
    future_month = starting_month + future_month
    print("The month will be", list_of_months[future_month-1])
