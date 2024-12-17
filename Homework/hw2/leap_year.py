"""
File:    leap_year.py
Author:  Mathew Dawit
Date:    09/17/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
  Determines if a given year is a leap year.
"""

year = int(input("Enter a year: "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")

        else:
            print(year, "is not a leap year.")
    
    else:
        print(year, "is a leap year.")

else:
    print(year, "is not a leap year.")
