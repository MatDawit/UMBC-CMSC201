"""
File:    harry_potter.py
Author:  Mathew Dawit
Date:    09/16/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
  Determines what character you are from a restricted group of Hogwarts individuals.
"""


response = input("Are you a student at Hogwarts? ")

if response == "yes":
    response = input("Do you have a scar? ")
    if response == "yes":
        print("You are Harry Potter.")
    elif response == "no":
        response = input("Do you have red hair? ")
        if response == "yes":
            print("You are a Weasley.")
        elif response == "no":
            print("You are Hermoine Granger.")

elif response == "no":
    response = input("Are you a teacher at Hogwarts? ")
    if response == "yes":
        response = input("Do you have a beard? ")
        if response == "yes":
            response = input("Are you part giant? ")
            if response == "yes":
                response = input("You are Rubius Hagrid.")
            elif response == "no":
                print("You are Albert Dumbledore.")
        elif response == "no":
            response = input("Do you give off evil vibes? ")
            if response == "yes":
                print("You are Severus Snape.")
            elif response == "no":
                print("You are Minerva McGonagall.")
    elif response == "no":
        print("You are Sirius Black.")
    
