"""
File:    pascal.py
Author:  Mathew Dawit
Date:    10/10/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
    The program calculates the next level of Pascal's triangle from a given list of
    integers (whether or not the input is part of Pascal's triangle) by summing adjacent
    elements and appending 1 at the start and end.
"""

def next_level(level):
    """
    A function to find the next level of inputed integers based on pascal's triangle
    :param level: the list of integers to update to the next level of pascal's triangle
    :return: the next level of the integers
    """

    next_level = [level[0]]
    
    for i in range(len(level)):
        if i < len(level)-1:
            next_level.append(level[i]+level[i+1])

        elif i == len(level)-1:
            next_level.append(level[i])

    return next_level
        

if __name__ == '__main__':
    in_string = input('What values do you want to run next_level on? ')

    while in_string != '':
        values = []

        for x in in_string.split():
            values.append(int(x))

        print(next_level(values))
        in_string = input('What values do you want to run next_level on? ')
