"""
File:    pupper_walks.py
Author:  Mathew Dawit
Date:    09/08/24
Section: 74
E-mail:  mdawit1@umbc.edu
Description:
  Calculates how long user walks their pupper every year
"""


pupper_real_name = input("What is pupper's real name? ")
pupper_walk_per_week = input("How many times per week do you walk pupper? ")
walk_distance_miles = input("How long is the walk in miles? ")
walk_time_minutes = input("How many minutes does it take for you to walk a mile? ")

yearly_walk_distance_miles = float(pupper_walk_per_week) * float(walk_distance_miles) * 52
yearly_walk_time_hours = yearly_walk_distance_miles * float(walk_time_minutes) / 60

print("Your dog's name is", pupper_real_name + ", and you have walked for", yearly_walk_distance_miles, "miles this year, in", yearly_walk_time_hours, "hours.")
