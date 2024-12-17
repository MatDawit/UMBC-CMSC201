"""
File:    ascending.py
Author:  Mathew Dawit
Date:    11/05/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
    The program checks if all elements in a list are in ascending order.
"""

def ascending(current_list, start=0):
    """
    A function to see if a number in ascending order is greater then the number before it
    :param current_list: the current list ascention
    :param start: the int start number 0
    :return: True or False
    """
    if len(current_list) <= 1:
        return True
    
    elif start == len(current_list) - 1:
        return True
    
    elif current_list[start] > current_list[start+1]:
        return False
    
    return ascending(current_list, start+1)


if __name__ == '__main__':
    print(ascending([1, 2, 3, 4, 5, 6]))
    print(ascending([1, 2, 3, 4, 4, 4, 4, 5, 6]))
    print(ascending([1, 2, 3, 4, 4, 4, 4, 1, 1, 1, 5, 6]))
    print(ascending([1, 2, 4, 8, 16, 32, 64, 128]))
    print(ascending([10, 9, 8, 7, 6, 5, 4]))
    print(ascending([]))
