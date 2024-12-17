"""
File:    connect_four.py
Author:  Mathew Dawit
Date:    10/10/24
Section: 70
E-mail:  mdawit1@umbc.edu
Description:
    The program checks if a player has won in Connect Four by finding four consecutive vertical or
    horizontal symbols in a 2D grid for a given player.
"""
def connect_four(the_grid, player_symbol):
    """
    A function to find four consecutive vertical or horizontal symbols in a 2D grid
    :param the_grid: a 2D grid with symbols on it
    :param player_symbol: the character the player uses
    :return: True or False
    """

    winning_symbol = player_symbol * 4
    for rows in range(len(the_grid)):

        if winning_symbol in the_grid[rows]:
            return True

        if len(the_grid) >= rows+3:
            for columns in range(len(the_grid[rows])):
                if player_symbol in the_grid[rows][columns]:
                    if player_symbol in the_grid[rows+1][columns]:
                        if player_symbol in the_grid[rows+2][columns]:
                            if player_symbol in the_grid[rows+3][columns]:
                                return True

    return False


if __name__ == '__main__':
    
    grid_rows = int(input("How many rows will be entered? "))
    grid = []

    while grid_rows <= 0:
        print("You have to input a number greater than or equal to 1.")
        grid_rows = int(input("How many rows will be entered? "))

    player_symbol = input("What do you want your symbol to be? ")

    for i in range(grid_rows):
        grid.append(input(""))

    print(connect_four(grid, player_symbol))
