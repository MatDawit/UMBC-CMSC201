"""
File:    burger.py
Author:  Mathew Dawit
Date:    09/30/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
    Build a burger layer by layer, count layers and condiments, and determine if it's a hamburger or cheeseburger.
"""

    
        


if __name__ == "__main__":
    burger_count = 0
    has_cheese = False
    condiments = []
    condiments_no_duplicates = []

    bottom_bun = input("What do you want to add? ")
    while bottom_bun != "bottom bun":
        print("You must start with the bottom bun!")
        bottom_bun = input("What do you want to add? ")

    top_bun = ""
    while top_bun != "top bun":
        top_bun = input("What do you want to add? ")
        if top_bun == "burger":
            burger_count += 1
        elif top_bun == "cheese":
            has_cheese = True
        elif top_bun == "top bun":
            True
        else:
            condiments.append(top_bun)

    print("You have created a", burger_count, end="")
    if has_cheese:
        print("-cheeseburger with the condiments: ", end="")
    else:
        print("-hamburger with the condiments: ", end="")
    if len(condiments) == 0:
        print("No Condiments")
    else:
        for x in condiments:
            if x not in condiments_no_duplicates:
                condiments_no_duplicates.append(x)
        
        for x in range(len(condiments_no_duplicates)):
            if len(condiments_no_duplicates)-1 == x:
                print(condiments_no_duplicates[x])
            else:
                print(condiments_no_duplicates[x] + ", ", end="")
