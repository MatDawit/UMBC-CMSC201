"""
File:    slice_of_pi.py
Author:  Mathew Dawit
Date:    09/22/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description: Determines approximation of pi using a certain formula
"""

upper_limit = int(input("Enter a positive integer L: "))
upper_limit_eqn = 0

for x in range(upper_limit+1):
    upper_limit_eqn = upper_limit_eqn + ((-1)**x)/(2*x+1)

print("The sum up to L =", upper_limit, "of the Leibniz formula is: ")
print(upper_limit_eqn)
print("This gives our approximation of pi as", upper_limit_eqn * 4)
