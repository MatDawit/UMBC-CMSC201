"""
File:    quasipal.py
Author:  Mathew Dawit
Date:    11/05/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
    The program checks if a word can become a palindrome by changing up
    to a specified number of letters.
"""


def quasi_palindrome(word, errors):
    """
    A function to find if a word is a palindrome based on amount of errors
    :param word: word to test if a palindrome
    :param errors: amount of errors to allow in palindrome
    :return: True or False
    """
    word = "".join("".join(word.split("'")).split())

    if len(word) <= 1:
        return True

    if word[0] != word[len(word)-1]:
        errors -= 1

        if errors < 0:
            return False
        
    return quasi_palindrome(word[1:-1], errors)



    


if __name__ == '__main__':
    word = input("What word do you want to check? ")

    while len(word.split()) == 2:
        print("Only enter 1 word.")
        word = input("What word do you want to check? ")

    errors = int(input("How many errors do you want to allow? "))

    while errors <= -1:
        print("You have to input a number greater than or equal to 0.")
        errors = int(input("How many errors do you want to allow? "))

    if quasi_palindrome(word, errors):
        print("It was a", str(errors) + "-quasi-palindrome!")

    else:
        print("It was not a", str(errors) + "-quasi-palindrome!")
