"""
File:    triangular.py
Author:  Mathew Dawit
Date:    11/05/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
    The program calculates numbers in a custom triangular sequence based on recursion.
"""


def triangular(num):
    """
    A function a certain number in a pattern
    :param num: a list
    :return: a number
    """
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 3
    return (3*triangular(num-1))-(3*triangular(num-2))+triangular(num-3)

if __name__ == '__main__':
   for i in range(20):
       print(i, triangular(i))
