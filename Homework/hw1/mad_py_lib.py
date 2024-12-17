"""
File:    mad_py_lib.py
Author:  Mathew Dawit
Date:    09/08/24
Section: 74
E-mail:  mdawit1@umbc.edu
Description:
  Creates a mad-lib using user inputs.
"""

user_name = input("Tell me your name: ")
subject = input("Tell me a subject/thing (noun): ")
adjective = input("Tell me an adjective: ")
verb = input("Tell me a verb: ")
noun = input("Tell me a noun: ")

print("Hello", user_name + ", we are going to have an amazing semester learning", subject + ", it's going to be", adjective, "so don't worry if you need to", verb, "from a", noun + ".")
