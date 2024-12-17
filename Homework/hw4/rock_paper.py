"""
File:    rock_paper.py
Author:  Mathew Dawit
Date:    09/30/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
    Plays rock, paper, scissors
"""

import sys
from random import choice, seed

if len(sys.argv) >= 2:
        seed(sys.argv[1])

if __name__ == "__main__":
    option = ""
    the_choice = choice(['rock', 'paper', 'scissors']) 

    while option != "stop":

        the_choice = choice(['rock', 'paper', 'scissors'])
        option = input("Enter rock, paper, or scissors to play, stop to end. ")

        
        if option == the_choice:
            print("Both", option, "there is a tie.")
        elif option != "stop" and option != "rock" and option != "paper" and option != "scissors":
            print("You need to select rock, paper or scissors.")
        elif option == "paper" and the_choice == "rock":
            print("Paper covers rock, you win.")
        elif option == "rock" and the_choice == "paper":
            print("Paper covers rock, you lose.")
        elif option == "rock" and the_choice == "scissors":
            print("Rock crushes scissors, you win.")
        elif option == "scissors" and the_choice == "rock":
            print("Rock crushes scissors, you lose.")
        elif option == "scissors" and the_choice == "paper":
            print("Scissors cuts paper, you win.")
        elif option == "paper" and the_choice == "scissors":
            print("Scissors cuts paper, you lose.")


    
