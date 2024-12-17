"""
File:    quasi_palindrome.py
Author:  Mathew Dawit
Date:    10/10/24
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

    error_count = 0
    word = "".join("".join(word.split("'")).split())

    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            error_count += 1

    if error_count > errors:
        return False
    
    else:
        return True
    

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
