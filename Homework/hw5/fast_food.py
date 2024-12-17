"""
File:    fast_food.py
Author:  Mathew Dawit
Date:    10/10/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
  The program calculates the total cost of a fast food order based on specific item types
  (burger, fries, drink, or combo), returning the final price instead of printing it.
"""

def is_combo(option_one, option_two, option_three):
    """
    A function to find options are a combo
    :param option_one: the first option
    :param option_two: the second option
    :param option_three: the third option
    :return: True or False
    """

    if  "burger" in option_one or "sandwich" in option_one:
        if "fries" in option_two:
            if option_three == "coke" or option_three == "sprite" or option_three == "mountain dew":
                return True
            
        elif option_two == "coke" or option_two == "sprite" or option_two == "mountain dew":
            if "fries" in option_three:
                return True
    
    elif option_one == "coke" or option_one == "sprite" or option_one == "mountain dew":
        if "fries" in option_two:
            if "burger" in option_three or "sandwich" in option_three:
                return True
        
        elif "burger" in option_two or "sandwich" in option_two:
            if "fries" in option_three:
                return True
            
    elif "fries" in option_one:
        if option_two == "coke" or option_two == "sprite" or option_two == "mountain dew":
            if "burger" in option_three or "sandwich" in option_three:
                return True
            
        elif "burger" in option_two or "sandwich" in option_two:
            if option_three == "coke" or option_three == "sprite" or option_three == "mountain dew":
                return True
    
    return False


def fast_food_receipt(order):
    """
    A function to find the price of an order
    :param order: items to be ordered
    :return: price of order
    """

    price = 0.0
    i = 0

    while i < len(order):
        
        if i < (len(order)-2) and is_combo(order[i], order[i+1], order[i+2]):
            price += 8.50
            i += 3

        elif ("burger" in order[i]) or ("sandwich" in order[i]):
            price += 5.00
            i += 1

        elif "fries" in order[i]:
            price += 3.00
            i += 1

        elif "coke" == order[i] or "sprite" == order[i] or "mountain dew" == order[i]:
            price += 2.50
            i += 1

        else:
            price += 4.00
            i += 1

    return price

if __name__ == '__main__':
    order = []
    user_input = ""

    while user_input != "place order":
        user_input = input("What would you like to order? ")
        order.append(user_input)

    order.remove("place order")
    receipt = fast_food_receipt(order)
    print("The total bill is", receipt)
