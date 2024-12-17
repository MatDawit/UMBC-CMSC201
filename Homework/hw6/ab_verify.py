"""
File:    ab_verify.py
Author:  Mathew Dawit
Date:    11/05/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
   The program checks if a string of 'a's and 'b's has more 'a's than 'b's at every point.
"""

def ab_verify(string, num):
   """
    A function to find if a word has a greater about of a's then b's
    :param string: a string of a's and b's
    :param num: number of a's and b's
    :return: True or False
    """
   if len(string) == 0:
      return num > -1
   elif num < 0:
      return False
   elif string[0] == 'a':
      num += 1
   elif string[0] == 'b':
      num -= 1

   return ab_verify(string[1:], num)


s = input('Enter a string to test: ')
while s != 'quit':
   print(ab_verify(s, 0))
   s = input('Enter a string to test: ')
