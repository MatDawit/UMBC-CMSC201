"""
File:    factor_me.py
Author:  Mathew Dawit
Date:    09/30/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
    Factor a number into primes less than 50, leaving larger factors unfactored.
"""


if __name__ == "__main__":
    
    primes_less_than_fifty = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    factorable_num = []
    num_to_factor = int(input("Enter a number to factor: "))
    same_num_check = num_to_factor

    for x in primes_less_than_fifty:
        while num_to_factor % x == 0:
            num_to_factor = int(num_to_factor / x)
            factorable_num.append(x)
        
    if num_to_factor == same_num_check:
        print("We didn't find any factors")
        print("This part of the number couldn't be factored with primes less than 50:", num_to_factor)
    elif num_to_factor != 1:
        print("The factors are: ", end="")
        for x in range(len(factorable_num)):
                if len(factorable_num)-1 == x:
                    print(factorable_num[x])
                else:
                    print(str(factorable_num[x]) + "*", end="")
        print("This part of the number couldn't be factored with primes less than 50:", num_to_factor)
    elif num_to_factor == 1:
        print("The factors are: ", end="")
        for x in range(len(factorable_num)):
                if len(factorable_num)-1 == x:
                    print(factorable_num[x])
                else:
                    print(str(factorable_num[x]) + "*", end="")
    
