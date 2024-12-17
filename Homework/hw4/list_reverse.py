"""
File:    list_reverse.py
Author:  Mathew Dawit
Date:    09/30/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
    Reverses and removes the numbers in a list and displays it
"""



if __name__ == "__main__":
    string_list = input("Enter a list separated by commas: ")
    string_list = string_list.split(",")
    dup_string_list = []
    new_list = []
    num = "0123456789"
    
    for y in range(len(string_list)):
        dup_string_list.insert(0, string_list[y])
            
    for y in range(len(dup_string_list)):
        for i in dup_string_list[y]:
            if i in num:
                dup_string_list[y] = ""
        if dup_string_list[y] != "":
            new_list.append(dup_string_list[y])
                

    if len(new_list) == 0:
        print("The new list was empty")
    else:
        print(", ".join(new_list))

