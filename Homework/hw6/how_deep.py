"""
File:    how_deep.py
Author:  Mathew Dawit
Date:    11/05/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
    The program calculates the depth of a nested list.
"""


def how_deep(list_struct):
    """
    A function to find how deep a list is
    :param list_struct: a list
    :return: highest_depth
    """
    if len(list_struct) == 0:
        return 1

    highest_depth = 0
    for i in range(len(list_struct)):
        curr_depth = 1 + how_deep(list_struct[i])

        if curr_depth > highest_depth:
            highest_depth = curr_depth

    return highest_depth


if __name__ == '__main__':
    print(how_deep([[[], [], [], [[[]]]], []]))
    print(how_deep([]))
    print(how_deep([[], []]))
    print(how_deep([[[]], [], [[]], [[[]]]]))
    print(how_deep([[[[], [[]], [[[]]], [[[[]]]]]]]))
    print(how_deep([[[], []], [], [[], []]]))
