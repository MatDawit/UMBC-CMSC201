"""
File:    padovan.py
Author:  Mathew Dawit
Date:    09/30/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
    Use the Padovan sequence to find a number
"""



if __name__ == "__main__":
    p_one = 1
    p_two = 1
    p_three = 1
    p_n = 0
    step = 3


    padovan_number_goal = int(input("Enter the goal to reach in the Padovan sequence: "))

    if padovan_number_goal == 1:
        print("It takes 1 step to get there or above.")
    else:
        while padovan_number_goal >= p_n:
            if padovan_number_goal >= p_n:
                p_n = p_one + p_two
                p_one = p_n
                step += 1
            if padovan_number_goal >= p_n:
                p_n =  p_two + p_three
                p_two = p_n
                step += 1
            if padovan_number_goal >= p_n:
                p_n = p_one + p_three
                p_three = p_n
                step += 1
        print("It takes", step, "step to get there or above.")



