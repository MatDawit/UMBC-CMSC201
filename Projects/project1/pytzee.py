"""
File:    pytzee.py
Author:  Mathew Dawit
Date:    10/23/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
  Program recreates the famous game Yahtzee but simplified
"""


import random

TOTAL_DICE = 5
DICE_FACES = 6
THREE_OF_A_KIND = ["three of a kind", "3 of a kind"]
FOUR_OF_A_KIND = ["four of a kind", "4 of a kind"]
SKIP = "skip"
COUNT_ONE = "1"
COUNT_TWO = "2"
COUNT_THREE = "3"
COUNT_FOUR = "4"
COUNT_FIVE = "5"
COUNT_SIX = "6"
CHANCE = "chance"
SMALL_STRAIGHT = "small straight"
LARGE_STRAIGHT = "large straight"
FULL_HOUSE = "full house"
PYTZEE = "pytzee"


def roll_dice():
    """
    :return: a list containing five integers representing dice rolls between 1 and 6.
    """

    roll_list = []

    for i in range(TOTAL_DICE):
        roll_list.append(random.randint(1, 6))

    return roll_list


def dice_sorter(list, keep_dup):
    """
    A function to sort a list of numbers
    :param list: the list to sort
    :param keep_dup: checks if user want to keep duplicates in list
    :return: a list sorted numbers
    """
    
    dup_dice_list = []
    no_dup_dice_list = []

    for num in range(1,7):
        dice_result_list = []
        
        for element in list:
            if num == element:
                dice_result_list.append(num)

                if num not in no_dup_dice_list:
                    no_dup_dice_list.append(num)

        if dice_result_list:
            dup_dice_list.append(dice_result_list)

    if keep_dup:
        return dup_dice_list
    
    else:
        return no_dup_dice_list


def score_insert(list, option, points):
    """
    A function to swaps points with a specific option
    :param list: a list of numbers
    :param option: the user choice
    :param points: a list of points
    """
    
    counter = 0

    if option in [COUNT_ONE, COUNT_TWO, COUNT_THREE, COUNT_FOUR, COUNT_FIVE, COUNT_SIX]:
        for num in range(1,7):
            if int(option) == num:
                for element in list:
                    if element == num:
                        counter += 1
                points[num-1] = counter*num
    
    elif option in FOUR_OF_A_KIND or option == CHANCE or option in THREE_OF_A_KIND:
        if option in FOUR_OF_A_KIND:
            points[7] = sum(list)

        elif option in THREE_OF_A_KIND:
            points[6] = sum(list)
        
        elif option == CHANCE:
            points[12] = sum(list)
    
    elif option == SMALL_STRAIGHT:
        points[9] = 30
            
    elif option == LARGE_STRAIGHT:
        points[10] = 40

    elif option == PYTZEE:
        if points[11] > 0:
            points[11] += 100

        else:
            points[11] = 50

    elif option == FULL_HOUSE:
        points[8] = 25


def scorecard(points):
    """
    A function print a score sheet
    :param points: a list of points
    """

    print("")
    print("\tScorecard:")
    print("1's\t2's\t3's\t4's\t5's\t6's")

    for point in range(len(points)//2):
        print(points[point], end="\t")
    
    print("\n")
    print("Three of a Kind\tFour of a Kind\tFull House")

    for point in range(len(points)//2, len(points)//2 + 3):
        print(points[point], end="\t\t")

    print("\n")
    print("Small Straight\tLarge Straight\tPytzee\tChance")

    for point in range(len(points)//2 + 3, len(points)):
        print(points[point], end="\t\t")

    print("\n")


def check_by_dice(list, option):
    """
    A function check if option is viable for dice faces
    :param list: a list of numbers
    :param option: the user choice
    :return: True or False if option is viable or not
    """

    dup_dice_list = dice_sorter(list, True)
    no_dup_dice_list = dice_sorter(list, False)

    if option in THREE_OF_A_KIND:
        for set in dup_dice_list:
            if len(set) >= 3:
                return True
        
    elif option in FOUR_OF_A_KIND:
        for set in dup_dice_list:
            if len(set) >= 4:
                return True
        
    elif option == PYTZEE:
        for set in dup_dice_list:
            if len(set) == 5:
                return True
            
    elif option == FULL_HOUSE:
        for set in dup_dice_list:
            if len(set) == 3:
                for second_set in dup_dice_list:
                    if len(second_set) == 2:
                        return True
                    
    elif option in [COUNT_ONE, COUNT_TWO, COUNT_THREE, COUNT_FOUR, COUNT_FIVE, COUNT_SIX]:
        for num in range(1,7):
            if int(option) == num and int(option) in no_dup_dice_list:
                return True
    
    elif option == CHANCE:
        return True
    
    elif option == SMALL_STRAIGHT:
        if (1 in no_dup_dice_list and 2 in no_dup_dice_list
                and 3 in no_dup_dice_list and 4 in no_dup_dice_list):
            return True
        
        elif (2 in no_dup_dice_list and 3 in no_dup_dice_list
                and 4 in no_dup_dice_list and 5 in no_dup_dice_list):
            return True
        
        elif (3 in no_dup_dice_list and 4 in no_dup_dice_list
                and 5 in no_dup_dice_list and 6 in no_dup_dice_list):
            return True
    
    elif option == LARGE_STRAIGHT:
        if (1 in no_dup_dice_list and 2 in no_dup_dice_list
                and 3 in no_dup_dice_list and 4 in no_dup_dice_list
                and 5 in no_dup_dice_list):
            return True
        
        elif (2 in no_dup_dice_list and 3 in no_dup_dice_list
                and 4 in no_dup_dice_list and 5 in no_dup_dice_list
                and 6 in no_dup_dice_list):
            return True
    
    elif option == SKIP:
        return True
    
    return False


def option_remover(options, option):
    """
    A function to remove the user choice from a list of options
    :param options: a list of options
    :param option: the user choice
    """
     
    if option in options and option != SKIP and option != PYTZEE:
        options.remove(option)

        if option == THREE_OF_A_KIND[0]:
            options.remove(THREE_OF_A_KIND[1])

        elif option == THREE_OF_A_KIND[1]:
            options.remove(THREE_OF_A_KIND[0])

        elif option == FOUR_OF_A_KIND[0]:
            options.remove(FOUR_OF_A_KIND[1])

        elif option == FOUR_OF_A_KIND[1]:
            options.remove(FOUR_OF_A_KIND[0])


def play_game(num_rounds):
    """
    A function to play the game
    :param num_rounds: number of rounds to play game
    """

    score = 0
    scorecard_points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    options_list = ["1", "2", "3", "4", "5",
                    "6", "chance", "pytzee", "small straight",
                    "large straight", "full house", "three of a kind",
                    "3 of a kind", "four of a kind", "4 of a kind", "skip"]

    for num in range(num_rounds):
        dice_list_as_str = []
        dice_list_as_int = []
        
        for dice in roll_dice():
            dice_list_as_str.append(str(dice))
            dice_list_as_int.append(dice)

        for points in scorecard_points:
            score += points

        if sum(scorecard_points[0:6]) >= 63:
            score += 35

        print("***** Beginning Round", num+1 ,"*****")
        print("\tYour score is:", score)
        print("\t".join(dice_list_as_str))
        user_option = input("How would you like to count this dice roll? ").strip().lower()

        if "count" in user_option[0:5] and len(user_option) <= 7:
            user_option = user_option[6]

        checks = True

        while checks:
            if user_option not in options_list:
                print("That choice is not an option or there is already a score in that slot.")

            elif not check_by_dice(dice_list_as_int, user_option):
                print("That choice is not possible with the dice you have.")

            else:
                checks = False

            if checks:
                user_option = input("How would you like to count this dice roll? ").strip().lower()

                if "count" in user_option[0:5] and len(user_option) == 7:
                    user_option = user_option[6]

        option_remover(options_list, user_option)
        
        if user_option == SMALL_STRAIGHT:
            print("You have a small straight and get 30 points.")

        elif user_option in [COUNT_ONE, COUNT_TWO, COUNT_THREE, COUNT_FOUR, COUNT_FIVE, COUNT_SIX]:
            print("Accepted the", user_option)

        elif user_option in THREE_OF_A_KIND:
            print("Three of a Kind!")

        elif user_option in FOUR_OF_A_KIND:
            print("Four of a Kind!")

        elif user_option == FULL_HOUSE:
            print("Full House!")

        elif user_option == LARGE_STRAIGHT:
            print("Your have a large straight and get 40 points.")

        elif user_option == PYTZEE:
            print("Pytzee!")

        score_insert(dice_list_as_int, user_option, scorecard_points)
        scorecard(scorecard_points)
        score = 0

    for points in scorecard_points:
        score += points

    if sum(scorecard_points[0:6]) >= 63:
        score += 35

    print("Your final score is", score)


if __name__ == '__main__':
    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to use a random seed: '))

    if seed:
        random.seed(seed)

    play_game(num_rounds)
