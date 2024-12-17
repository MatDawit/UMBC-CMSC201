"""
File:    wordle_checker.py
Author:  Mathew Dawit
Date:    09/22/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description: Checks if guess word is the solution word. Based of the famous New York Times game Wordle
"""

soln_word = input("Enter the solution word: ")
guess_word = input("Enter the guess word: ")
answer = []

if (len(soln_word) or len(guess_word)) <= 0:
    print("Word should be at least 1 character")
elif (len(soln_word)) > len(guess_word):
    print("Solution word is larger than guess word")
elif (len(soln_word)) < len(guess_word):
    print("Guess word is larger than solution word")
else:
    for x in range(len(soln_word)):
        if guess_word[x] == soln_word[x]:
            answer.append("g")
        elif guess_word[x] in soln_word:
            answer.append("y")
        elif guess_word[x] not in soln_word[x]:
            answer.append("_")
    print(answer)
