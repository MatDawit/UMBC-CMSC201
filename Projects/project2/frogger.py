"""
File:    frogger.py
Author:  Mathew Dawit
Date:    11/11/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
  The Frogger game lets the player control a frog trying to cross a road with moving cars.
  The frog can move using the keyboard or jump to a specific spot.
  The game ends when the frog reaches the other side or is hit by a car.
  The player has a limited number of jumps to help the frog succeed.
"""

FROG = '\U0001F438' # the emoji one
MOVESET = ['w', 'a', 's', 'd', 'j', '']

import os
from re import split
root, directories, files = next(os.walk('.'))


def game_options(game_file):
    """
    Reads the game configuration from a file and sets up the game parameters.
    
    :param game_file: the file containing the game settings and initial data
    :return: the number of rows, columns, available jumps, rotation speeds, cars, and initial frog position
    """


    with open(game_file, 'r') as file:
        game_file_info = file.readlines()
    rows = int(game_file_info[0].split()[0])
    columns = int(game_file_info[0].split()[1])
    jumps = int(game_file_info[0].split()[2])
    rotation_speed = []
    cars = []
    frog_pos = [0,columns//2]
    
    for i in range(len("".join((game_file_info[1]).split()))):
        rotation_speed.append(int(game_file_info[1].split()[i]))

    for i in range(2, 2+rows):
        cars.append(game_file_info[i][:columns])

    for i in range(len(cars)):
        temp_string = ""

        for y in range(columns):

            if cars[i][y] != 'X' and cars[i][y] != '_':
                temp_string += 'X'

            elif cars[i][y] != 'X' and cars[i][y] == '_':
                temp_string += '_'

            else:
                temp_string += 'X'

        cars[i] = temp_string
        
    cars.insert(0, " "*columns)
    cars.append(" "*columns)
    str_list = list(cars[0])
    str_list[frog_pos[1]] = FROG
    
    return rows, columns, jumps, rotation_speed, cars, frog_pos


def movement_check(columns, frog_pos, jumps, move_list):
    """
    Validates the player's movement input to ensure it's within the game rules.
    
    :param columns: the number of columns in the game grid
    :param frog_pos: the current position of the frog as a list [row, column]
    :param jumps: the number of remaining jumps the frog can make
    :param move_list: the list containing the player's movement input
    :return: True if the movement is valid, False otherwise
    """


    def is_number(string):
        for char in string:
            if char not in '0123456789':
                return False
            
        return True

    if move_list[0] not in MOVESET:
        print("Invalid Move.")
        return False

    elif move_list[0] == 'j':
        if len(move_list) != 3:
            print("Invalid Jump: Move must contain exactly three elements.")
            return False
        
        elif jumps == 0:
            print("Invalid Jump: No jumps remaining.")
            return False
        
        elif not is_number(move_list[1]) or not is_number(move_list[2]):
            print("Invalid Jump: Rows and Columns coordinates must be a number.")
            return False
        
        elif not ((int(move_list[1]) - frog_pos[0]) in [-1, 0, 1]):
            print("Invalid Jump: Rows coordinate must be within [-1, 0, 1] of frog position rows.")
            return False
        
        elif int(move_list[2]) == 0:
            print("Invalid Jump: Columns coordinate cannot be 0.")
            return False

        elif int(move_list[1]) < 0 or int(move_list[2]) < 0:
            print("Invalid Jump: Rows and Columns coordinate must be non-negative.")
            return False
        
        elif int(move_list[2]) > columns:
            print("Invalid Jump: Columns coordinate exceeds column limit.")
            return False

    elif move_list[0].lower() == 'd':
        if frog_pos[1] == columns-1:
            print("Invalid Move: Cannot move right, you're at the last column.")
            return False
        
        elif len(move_list) > 1:
            print("Invalid Move: Unknown Extra Values")
            return False
    
    elif move_list[0].lower() == 'w':
        if frog_pos[0] == 0:
            print("Invalid Move: Cannot move up, you're at the top row.")
            return False
    
        elif len(move_list) > 1:
            print("Invalid Move: Unknown Extra Values")
            return False
    
    elif move_list[0].lower() == 'a':
        if frog_pos[1] == 0:
            print("Invalid Move: Cannot move left, you're at the first column.")
            return False 
    
        elif len(move_list) > 1:
            print("Invalid Move: Unknown Extra Values")
            return False

    return True


def movement(frog_pos, columns, jumps):
    """
    Prompts the player to make a move, checks if it's valid, and updates the frog's position accordingly.
    
    :param frog_pos: the current position of the frog as a list [row, column]
    :param columns: the number of columns in the game grid
    :param jumps: the number of remaining jumps the frog can make
    :return: the updated number of jumps remaining
    """


    movement_option = input("WASDJ >> ").strip()
    move_list = movement_option.lower().split()

    if not move_list:
        move_list.append('')

    keyboard = movement_check(columns, frog_pos, jumps, move_list)

    while not keyboard:
        movement_option = input("WASDJ >> ").strip()
        move_list = movement_option.lower().split()

        if not move_list:
            move_list.append('')

        keyboard = movement_check(columns, frog_pos, jumps, move_list)

    if movement_option.lower() == 'w':
        frog_pos[0] = int(frog_pos[0] - 1)

    elif movement_option.lower() == 'a':
        frog_pos[1] = int(frog_pos[1] - 1)

    elif movement_option.lower() == 's':
        frog_pos[0] = int(frog_pos[0] + 1)

    elif movement_option.lower() == 'd':
        frog_pos[1] = int(frog_pos[1] + 1)

    elif move_list[0] == 'j':
        frog_pos[1] = int(move_list[2]) - 1
        frog_pos[0] = int(move_list[1])
        jumps -= 1

    elif movement_option.strip() == '':
        pass

    return jumps
    

def list_recreator(cars, cars_original, curr_frog_pos):
    """
    Updates the game board by moving the frog to its new position and checks if it has won or lost.
    
    :param cars: the current state of the cars on the game grid
    :param cars_original: the original state of the cars
    :param curr_frog_pos: the current position of the frog as a list [row, column]
    :return: the updated list of cars and a string indicating the game status ('won', 'lost', or 'continue')
    """
    

    char_that_was_hit = cars_original[curr_frog_pos[0]][curr_frog_pos[1]]
    cars = cars_original[:]    
    str_list = list(cars[curr_frog_pos[0]])    
    str_list[curr_frog_pos[1]] = FROG
    cars[curr_frog_pos[0]] = ''.join(str_list)

    if FROG in cars[len(cars)-1]:
        return cars, 'won'
    
    elif char_that_was_hit == 'X':
        return cars, 'lost'
    
    else:
        return cars, 'continue'


def display_board(cars, cars_original, curr_frog_pos):
    """
    Displays the game board with the updated position of the frog.
    
    :param cars: the current state of the cars on the game grid
    :param cars_original: the original state of the cars
    :param curr_frog_pos: the current position of the frog as a list [row, column]
    :return: a string indicating whether the frog has won, lost, or should continue
    """
     
    
    cars, hit = list_recreator(cars, cars_original, curr_frog_pos)
    for car_row in cars:
        for car in car_row:
            print(f"{car}", end=' ')

        print()

    return hit


def select_game_file():
    """
    Prompts the user to select a game configuration file from the available options.
    
    :return: the selected game file name
    """


    choices = []

    for i in range(len(files)):
        if '.frog' in files[i]:
            choices.append(str(i+1))
            print(f"[{i+1}]  	{files[i]}")
    
    option = input("Enter an option: ")

    while option not in choices:
        option = input("Not an option. Enter another option: ")
       
    for i in range(len(files)):
        if int(option) == i+1:
            return files[i]


def rotations(cars, rotation_speed):
    """
    Rotates the cars on the game board based on the specified rotation speeds.
    
    :param cars: the current state of the cars on the game grid
    :param rotation_speed: the list of rotation speeds for each row of cars
    :return: None (modifies the cars list in-place)
    """
     

    for i in range(1,len(cars)-1):
        temp_list = cars[i][-rotation_speed[i-1]:] + cars[i][:-rotation_speed[i-1]]
        cars[i] = temp_list


def frogger_game(game_file):
    """
    Main game loop for the Frogger game, managing the game rounds, player movements, and game status.
    
    :param game_file: the file containing the game settings and initial data
    :return: None
    """


    rounds = 1
    game = 'continue'
    rows, columns, jumps, rotation_speed, cars, frog_pos = game_options(game_file)
    cars_original = list(cars)

    while game != 'won' and game != 'lost':
        print(rounds)
        
        game = display_board(cars, cars_original, frog_pos)

        if game == 'continue':
            rotations(cars, rotation_speed)
            rotations(cars_original, rotation_speed)
            jumps = movement(frog_pos, columns, jumps)
            rounds += 1

    if game == 'won':
        print("You won, Frog lives to cross another day.")

    else:
        print("You Lost, Sorry Frog")
       

if __name__ == '__main__':
   selected_game_file = select_game_file()
   frogger_game(selected_game_file)
