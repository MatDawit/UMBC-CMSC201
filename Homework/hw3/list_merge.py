"""
File:    list_merge.py
Author:  Mathew Dawit
Date:    09/22/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description: Program merges two lists
"""

elements_in_list = int(input("How  many elements do you want in each list? "))
first_list = []
second_list = []

for i in range(elements_in_list):
    first_list.append(input("What do you want to put in the first list? "))

for i in range(elements_in_list):
    second_list.append(input("What do you want to put in the second list? "))

merged_list = first_list + second_list

print("The first list is:", first_list)
print("The second list is:", second_list)
print("The merged list is:", merged_list)
