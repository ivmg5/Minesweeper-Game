"""This module contains the functions and classes for the Integrative Project."""

# Import os because it will be necessary for the clear_screen() function to work
import os

def main():
    """Create the three boards: the one that will change as the game progresses, a board showing how it should look when the user wins (to compare and know if they've won), and the one with hidden data."""
    hidden_board = [
        [' ',' ',' ',' ',' ',' ','1','X','2','1',' ',' ','1','X','2','X','X','1','1','2','2','1','1','1','2','X','3','X','4','2','1'],
        [' ',' ',' ',' ',' ',' ','2','4','X','2',' ',' ','2','2','4','4','4','3','2','X','X','2','2','X','2','1','4','X','X','X','1'],
        [' ',' ',' ',' ','1','1','2','X','X','2',' ',' ','1','X','3','X','X','3','X','3','2','2','X','2','1',' ','3','X','5','2','1'],
        ['1','1',' ',' ','1','X','3','3','3','1',' ',' ','1','2','X','4','X','4','2','2',' ','2','2','2',' ',' ','2','X','2',' ',' '],
        ['X','1',' ',' ','2','3','4','X','1','1','1','1',' ','1','1','2','1','2','X','1',' ','2','X','2',' ',' ','1','1','1',' ',' '],
        ['2','2',' ',' ','1','X','X','2','1','1','X','2','1','1',' ',' ',' ','2','2','2',' ','3','X','3','1','1','2','1','2','1','1'],
        ['X','2','1',' ','2','3','3','1',' ','1','2','3','X','2','1','1',' ','1','X','1',' ','2','X','3','2','X','2','X','3','X','2'],
        ['2','X','1',' ','1','X','1',' ','1','1','2','X','2','3','X','2',' ','1','1','1',' ','1','2','X','2','2','4','4','5','X','3'],
        ['2','2','2','1','2','1','2','1','2','X','2','1','1','2','X','3','1','1',' ',' ',' ',' ','1','1','1','1','X','X','X','4','X'],
        ['X','1','1','X','1',' ','2','X','3','1','1',' ',' ','1','2','3','X','1',' ','1','1','1',' ',' ',' ','1','2','3','2','4','X'],
        ['1','1','1','2','2','1','2','X','3','1',' ',' ','1','1','2','X','3','2','1','1','X','1','1','2','3','2','1',' ',' ','3','X'],
        ['1','1','1','3','X','2','1','2','X','1',' ',' ','1','X','2','2','3','X','3','3','2','1','1','X','X','X','1',' ',' ','2','X'],
        ['X','2','2','X','X','4','1','1','1','1',' ','1','2','3','2','3','X','5','X','X','2',' ','1','2','4','4','3','1',' ','1','1'],
        ['1','2','X','4','X','X','2',' ','1','1','1','2','X','3','X','3','X','4','X','X','2',' ','1','1','2','X','X','2','2','1','1'],
        [' ','1','1','2','4','X','4','1','1','X','2','3','X','3','1','2','1','2','2','3','2','2','2','X','3','3','4','X','4','X','1'],
        [' ',' ',' ',' ','2','X','X','1','1','1','2','X','2','1',' ',' ',' ',' ',' ','1','X','2','X','3','X','1','2','X','X','2','1']
    ]

    win_board = [
        [' ',' ',' ',' ',' ',' ','1','_','2','1',' ',' ','1','_','2','_','_','1','1','2','2','1','1','1','2','_','3','_','4','2','1'],
        [' ',' ',' ',' ',' ',' ','2','4','_','2',' ',' ','2','2','4','4','4','3','2','_','_','2','2','_','2','1','4','_','_','_','1'],
        [' ',' ',' ',' ','1','1','2','_','_','2',' ',' ','1','_','3','_','_','3','_','3','2','2','_','2','1',' ','3','_','5','2','1'],
        ['1','1',' ',' ','1','_','3','3','3','1',' ',' ','1','2','_','4','_','4','2','2',' ','2','2','2',' ',' ','2','_','2',' ',' '],
        ['_','1',' ',' ','2','3','4','_','1','1','1','1',' ','1','1','2','1','2','_','1',' ','2','_','2',' ',' ','1','1','1',' ',' '],
        ['2','2',' ',' ','1','_','_','2','1','1','_','2','1','1',' ',' ',' ','2','2','2',' ','3','_','3','1','1','2','1','2','1','1'],
        ['_','2','1',' ','2','3','3','1',' ','1','2','3','_','2','1','1',' ','1','_','1',' ','2','_','3','2','_','2','_','3','_','2'],
        ['2','_','1',' ','1','_','1',' ','1','1','2','_','2','3','_','2',' ','1','1','1',' ','1','2','_','2','2','4','4','5','_','3'],
        ['2','2','2','1','2','1','2','1','2','_','2','1','1','2','_','3','1','1',' ',' ',' ',' ','1','1','1','1','_','_','_','4','_'],
        ['_','1','1','_','1',' ','2','_','3','1','1',' ',' ','1','2','3','_','1',' ','1','1','1',' ',' ',' ','1','2','3','2','4','_'],
        ['1','1','1','2','2','1','2','_','3','1',' ',' ','1','1','2','_','3','2','1','1','_','1','1','2','3','2','1',' ',' ','3','_'],
        ['1','1','1','3','_','2','1','2','_','1',' ',' ','1','_','2','2','3','_','3','3','2','1','1','_','_','_','1',' ',' ','2','_'],
        ['_','2','2','_','_','4','1','1','1','1',' ','1','2','3','2','3','_','5','_','_','2',' ','1','2','4','4','3','1',' ','1','1'],
        ['1','2','_','4','_','_','2',' ','1','1','1','2','_','3','_','3','_','4','_','_','2',' ','1','1','2','_','_','2','2','1','1'],
        [' ','1','1','2','4','_','4','1','1','_','2','3','_','3','1','2','1','2','2','3','2','2','2','_','3','3','4','_','4','_','1'],
        [' ',' ',' ',' ','2','_','_','1','1','1','2','_','2','1',' ',' ',' ',' ',' ','1','_','2','_','3','_','1','2','_','_','2','1']
    ]
    empty_board = [
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_']
    ]
    # Welcome message
    print('WELCOME TO MINESWEEPER\n')
    # Create a variable with an initial value of 0, but it will change when wanting to exit the loop
    var = 1
    # Start the game loop, which will repeat until the user loses or wins
    while var == 1 and (win_board != empty_board):
        # Display the board so the user can choose a cell
        display_board(empty_board)
        # Ask for the row and column number to make a decision based on it
        print('INDICATE THE CELL YOU WANT TO REVEAL')
        row = int(input('ROW: '))
        column = int(input('COLUMN: '))
        # Call the function to perform the pertinent action depending on the cell chosen by the user
        value = check_values_and_reveal(row, column, empty_board, hidden_board)
        # Based on the result depending on what was in the chosen cell, decide whether to continue or not
        if value == 1:
            var = 1
        else:
            var += 1
    # Conditional to check if the expected board is equal to the current board to know if the user has won
    if win_board == empty_board:
        clear_screen()
        display_board(empty_board)
        print('YOU WON!')
def create_list():
    """Create the list of numbers used to show the column numbers and return it. This function is used inside the display_board() function."""
    list_ = []
    for i in range(1, 32):
        list_.append(i)
    return list_
def display_board(board):
    """Display the board along with the row and column numbers"""
    list_ = create_list()
    print('   ', end='')
    for element in list_:
        print(str(element).center(3), end='')
    count = 1
    for row in board:
        print("\n")
        print(str(count).center(2) + ' ', end="")
        count += 1
        print("|", end="")
        for element in row:
            print(f'{element}'.center(2), end='')
            print("|", end="")
    print("\n")
def check_values_and_reveal(row, column, empty_board, hidden_board):
    """Checks if the row and column are valid values (within cell range) and not repeated. Also, reveals the cell on the board. The function returns a 2 in case of an error or bomb and 1 when it is not."""
    if (1 <= row <= 16) and (1 <= column <= 31):
        position = hidden_board[row-1][column-1]
        current = empty_board[row-1][column-1]
        # The next if is triggered when the value has not been previously chosen
        if current == '_':
            # The next if is triggered when the cell chosen by the user does not correspond to a bomb
            if position != "X":
                # All the following ifs and elifs are triggered when the user chooses a cell that is blank
                if (1 <= column <= 6 and 1 <= row <= 2) or (row == 3 and 1 <= column <= 4) or (4 <= row <= 6 and 3 <= column <= 4) or (7 <= row <= 8 and column == 4):
                    empty_board[0][0] = hidden_board[0][0]
                    empty_board[0][1] = hidden_board[0][1]
                    empty_board[0][2] = hidden_board[0][2]
                    empty_board[0][3] = hidden_board[0][3]
                    empty_board[0][4] = hidden_board[0][4]
                    empty_board[0][5] = hidden_board[0][5]
                    empty_board[0][6] = hidden_board[0][6]
                    empty_board[1][0] = hidden_board[1][0]
                    empty_board[1][1] = hidden_board[1][1]
                    empty_board[1][2] = hidden_board[1][2]
                    empty_board[1][3] = hidden_board[1][3]
                    empty_board[1][4] = hidden_board[1][4]
                    empty_board[1][5] = hidden_board[1][5]
                    empty_board[1][6] = hidden_board[1][6]
                    empty_board[2][0] = hidden_board[2][0]
                    empty_board[2][1] = hidden_board[2][1]
                    empty_board[2][2] = hidden_board[2][2]
                    empty_board[2][3] = hidden_board[2][3]
                    empty_board[2][4] = hidden_board[2][4]
                    empty_board[2][5] = hidden_board[2][5]
                    empty_board[2][6] = hidden_board[2][6]
                    empty_board[3][0] = hidden_board[3][0]
                    empty_board[3][1] = hidden_board[3][1]
                    empty_board[3][2] = hidden_board[3][2]
                    empty_board[3][3] = hidden_board[3][3]
                    empty_board[3][4] = hidden_board[3][4]
                    empty_board[4][1] = hidden_board[4][1]
                    empty_board[4][2] = hidden_board[4][2]
                    empty_board[4][3] = hidden_board[4][3]
                    empty_board[4][4] = hidden_board[4][4]
                    empty_board[5][1] = hidden_board[5][1]
                    empty_board[5][2] = hidden_board[5][2]
                    empty_board[5][3] = hidden_board[5][3]
                    empty_board[5][4] = hidden_board[5][4]
                    empty_board[6][1] = hidden_board[6][1]
                    empty_board[6][2] = hidden_board[6][2]
                    empty_board[6][3] = hidden_board[6][3]
                    empty_board[6][4] = hidden_board[6][4]
                    empty_board[7][2] = hidden_board[7][2]
                    empty_board[7][3] = hidden_board[7][3]
                    empty_board[7][4] = hidden_board[7][4]
                    empty_board[8][2] = hidden_board[8][2]
                    empty_board[8][3] = hidden_board[8][3]
                    empty_board[8][4] = hidden_board[8][4]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif row == 10 and column == 6:
                    empty_board[8][4] = hidden_board[8][4]
                    empty_board[8][5] = hidden_board[8][5]
                    empty_board[8][6] = hidden_board[8][6]
                    empty_board[9][4] = hidden_board[9][4]
                    empty_board[9][5] = hidden_board[9][5]
                    empty_board[9][6] = hidden_board[9][6]
                    empty_board[10][4] = hidden_board[10][4]
                    empty_board[10][5] = hidden_board[10][5]
                    empty_board[10][6] = hidden_board[10][6]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif (row == 8 and column == 8) or (row == 7 and column == 9):
                    empty_board[5][7] = hidden_board[5][7]
                    empty_board[5][8] = hidden_board[5][8]
                    empty_board[5][9] = hidden_board[5][9]
                    empty_board[6][6] = hidden_board[6][6]
                    empty_board[6][7] = hidden_board[6][7]
                    empty_board[6][8] = hidden_board[6][8]
                    empty_board[6][9] = hidden_board[6][9]
                    empty_board[7][6] = hidden_board[7][6]
                    empty_board[7][7] = hidden_board[7][7]
                    empty_board[7][8] = hidden_board[7][8]
                    empty_board[7][9] = hidden_board[7][9]
                    empty_board[8][6] = hidden_board[8][6]
                    empty_board[8][7] = hidden_board[8][7]
                    empty_board[8][8] = hidden_board[8][8]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif row == 14 and column == 8:
                    empty_board[12][6] = hidden_board[12][6]
                    empty_board[12][7] = hidden_board[12][7]
                    empty_board[12][8] = hidden_board[12][8]
                    empty_board[13][6] = hidden_board[13][6]
                    empty_board[13][7] = hidden_board[13][7]
                    empty_board[13][8] = hidden_board[13][8]
                    empty_board[14][6] = hidden_board[14][6]
                    empty_board[14][7] = hidden_board[14][7]
                    empty_board[14][8] = hidden_board[14][8]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif (1 <= row <= 4 and 11 <= column <= 12) or (row == 5 and column == 13):
                    empty_board[0][9] = hidden_board[0][9]
                    empty_board[0][10] = hidden_board[0][10]
                    empty_board[0][11] = hidden_board[0][11]
                    empty_board[0][12] = hidden_board[0][12]
                    empty_board[1][9] = hidden_board[1][9]
                    empty_board[1][10] = hidden_board[1][10]
                    empty_board[1][11] = hidden_board[1][11]
                    empty_board[1][12] = hidden_board[1][12]
                    empty_board[2][9] = hidden_board[2][9]
                    empty_board[2][10] = hidden_board[2][10]
                    empty_board[2][11] = hidden_board[2][11]
                    empty_board[2][12] = hidden_board[2][12]
                    empty_board[3][9] = hidden_board[3][9]
                    empty_board[3][10] = hidden_board[3][10]
                    empty_board[3][11] = hidden_board[3][11]
                    empty_board[3][12] = hidden_board[3][12]
                    empty_board[3][13] = hidden_board[3][13]
                    empty_board[4][9] = hidden_board[4][9]
                    empty_board[4][10] = hidden_board[4][10]
                    empty_board[4][11] = hidden_board[4][11]
                    empty_board[4][12] = hidden_board[4][12]
                    empty_board[4][13] = hidden_board[4][13]
                    empty_board[5][11] = hidden_board[5][11]
                    empty_board[5][12] = hidden_board[5][12]
                    empty_board[5][13] = hidden_board[5][13]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif (row == 10 and 12 <= column <= 13) or (11 <= row <= 12 and 11 <= column <= 12) or (row == 13 and column == 11):
                    empty_board[8][10] = hidden_board[8][10]
                    empty_board[8][11] = hidden_board[8][11]
                    empty_board[8][12] = hidden_board[8][12]
                    empty_board[8][13] = hidden_board[8][13]
                    empty_board[9][9] = hidden_board[9][9]
                    empty_board[9][10] = hidden_board[9][10]
                    empty_board[9][11] = hidden_board[9][11]
                    empty_board[9][12] = hidden_board[9][12]
                    empty_board[9][13] = hidden_board[9][13]
                    empty_board[10][9] = hidden_board[10][9]
                    empty_board[10][10] = hidden_board[10][10]
                    empty_board[10][11] = hidden_board[10][11]
                    empty_board[10][12] = hidden_board[10][12]
                    empty_board[10][13] = hidden_board[10][13]
                    empty_board[11][9] = hidden_board[11][9]
                    empty_board[11][10] = hidden_board[11][10]
                    empty_board[11][11] = hidden_board[11][11]
                    empty_board[11][12] = hidden_board[11][12]
                    empty_board[12][9] = hidden_board[12][9]
                    empty_board[12][10] = hidden_board[12][10]
                    empty_board[12][11] = hidden_board[12][11]
                    empty_board[12][12] = hidden_board[12][12]
                    empty_board[13][9] = hidden_board[13][9]
                    empty_board[13][10] = hidden_board[13][10]
                    empty_board[13][11] = hidden_board[13][11]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif (row == 6 and 15 <= column <= 17) or (7 <= row <= 8 and column == 17):
                    empty_board[4][13] = hidden_board[4][13]
                    empty_board[4][14] = hidden_board[4][14]
                    empty_board[4][15] = hidden_board[4][15]
                    empty_board[4][16] = hidden_board[4][16]
                    empty_board[4][17] = hidden_board[4][17]
                    empty_board[5][13] = hidden_board[5][13]
                    empty_board[5][14] = hidden_board[5][14]
                    empty_board[5][15] = hidden_board[5][15]
                    empty_board[5][16] = hidden_board[5][16]
                    empty_board[5][17] = hidden_board[5][17]
                    empty_board[6][13] = hidden_board[6][13]
                    empty_board[6][14] = hidden_board[6][14]
                    empty_board[6][15] = hidden_board[6][15]
                    empty_board[6][16] = hidden_board[6][16]
                    empty_board[6][17] = hidden_board[6][17]
                    empty_board[7][15] = hidden_board[7][15]
                    empty_board[7][16] = hidden_board[7][16]
                    empty_board[7][17] = hidden_board[7][17]
                    empty_board[8][15] = hidden_board[8][15]
                    empty_board[8][16] = hidden_board[8][16]
                    empty_board[8][17] = hidden_board[8][17]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif row == 16 and 15 <= column <= 19:
                    empty_board[14][13] = hidden_board[14][13]
                    empty_board[14][14] = hidden_board[14][14]
                    empty_board[14][15] = hidden_board[14][15]
                    empty_board[14][16] = hidden_board[14][16]
                    empty_board[14][17] = hidden_board[14][17]
                    empty_board[14][18] = hidden_board[14][18]
                    empty_board[14][19] = hidden_board[14][19]
                    empty_board[15][13] = hidden_board[15][13]
                    empty_board[15][14] = hidden_board[15][14]
                    empty_board[15][15] = hidden_board[15][15]
                    empty_board[15][16] = hidden_board[15][16]
                    empty_board[15][17] = hidden_board[15][17]
                    empty_board[15][18] = hidden_board[15][18]
                    empty_board[15][19] = hidden_board[15][19]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif (4 <= row <= 8 and column == 21) or (row == 9 and 19 <= column <= 22) or (row == 10 and column == 19) or (row == 10 and 23 <= column <= 25):
                    empty_board[2][19] = hidden_board[2][19]
                    empty_board[2][20] = hidden_board[2][20]
                    empty_board[2][21] = hidden_board[2][21]
                    empty_board[3][19] = hidden_board[3][19]
                    empty_board[3][20] = hidden_board[3][20]
                    empty_board[3][21] = hidden_board[3][21]
                    empty_board[4][19] = hidden_board[4][19]
                    empty_board[4][20] = hidden_board[4][20]
                    empty_board[4][21] = hidden_board[4][21]
                    empty_board[5][19] = hidden_board[5][19]
                    empty_board[5][20] = hidden_board[5][20]
                    empty_board[5][21] = hidden_board[5][21]
                    empty_board[6][19] = hidden_board[6][19]
                    empty_board[6][20] = hidden_board[6][20]
                    empty_board[6][21] = hidden_board[6][21]
                    empty_board[7][17] = hidden_board[7][17]
                    empty_board[7][18] = hidden_board[7][18]
                    empty_board[7][19] = hidden_board[7][19]
                    empty_board[7][20] = hidden_board[7][20]
                    empty_board[7][21] = hidden_board[7][21]
                    empty_board[7][22] = hidden_board[7][22]
                    empty_board[8][17] = hidden_board[8][17]
                    empty_board[8][18] = hidden_board[8][18]
                    empty_board[8][19] = hidden_board[8][19]
                    empty_board[8][20] = hidden_board[8][20]
                    empty_board[8][21] = hidden_board[8][21]
                    empty_board[8][22] = hidden_board[8][22]
                    empty_board[8][23] = hidden_board[8][23]
                    empty_board[8][24] = hidden_board[8][24]
                    empty_board[8][25] = hidden_board[8][25]
                    empty_board[9][17] = hidden_board[9][17]
                    empty_board[9][18] = hidden_board[9][18]
                    empty_board[9][19] = hidden_board[9][19]
                    empty_board[9][20] = hidden_board[9][20]
                    empty_board[9][21] = hidden_board[9][21]
                    empty_board[9][22] = hidden_board[9][22]
                    empty_board[9][23] = hidden_board[9][23]
                    empty_board[9][24] = hidden_board[9][24]
                    empty_board[9][25] = hidden_board[9][25]
                    empty_board[10][17] = hidden_board[10][17]
                    empty_board[10][18] = hidden_board[10][18]
                    empty_board[10][19] = hidden_board[10][19]
                    empty_board[10][21] = hidden_board[10][21]
                    empty_board[10][22] = hidden_board[10][22]
                    empty_board[10][23] = hidden_board[10][23]
                    empty_board[10][24] = hidden_board[10][24]
                    empty_board[10][25] = hidden_board[10][25]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif 13 <= row <= 14 and column == 22:
                    empty_board[11][20] = hidden_board[11][20]
                    empty_board[11][21] = hidden_board[11][21]
                    empty_board[11][22] = hidden_board[11][22]
                    empty_board[12][20] = hidden_board[12][20]
                    empty_board[12][21] = hidden_board[12][21]
                    empty_board[12][22] = hidden_board[12][22]
                    empty_board[13][20] = hidden_board[13][20]
                    empty_board[13][21] = hidden_board[13][21]
                    empty_board[13][22] = hidden_board[13][22]
                    empty_board[14][20] = hidden_board[14][20]
                    empty_board[14][21] = hidden_board[14][21]
                    empty_board[14][22] = hidden_board[14][22]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif (4 <= row <= 5 and 25 <= column <= 26) or (row == 3 and column == 26):
                    empty_board[1][24] = hidden_board[1][24]
                    empty_board[1][25] = hidden_board[1][25]
                    empty_board[1][26] = hidden_board[1][26]
                    empty_board[2][23] = hidden_board[2][23]
                    empty_board[2][24] = hidden_board[2][24]
                    empty_board[2][25] = hidden_board[2][25]
                    empty_board[2][26] = hidden_board[2][26]
                    empty_board[3][23] = hidden_board[3][23]
                    empty_board[3][24] = hidden_board[3][24]
                    empty_board[3][25] = hidden_board[3][25]
                    empty_board[3][26] = hidden_board[3][26]
                    empty_board[4][23] = hidden_board[4][23]
                    empty_board[4][24] = hidden_board[4][24]
                    empty_board[4][25] = hidden_board[4][25]
                    empty_board[4][26] = hidden_board[4][26]
                    empty_board[5][23] = hidden_board[5][23]
                    empty_board[5][24] = hidden_board[5][24]
                    empty_board[5][25] = hidden_board[5][25]
                    empty_board[5][26] = hidden_board[5][26]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif (11 <= row <= 12 and 28 <= column <= 29) or (row == 13 and column == 29):
                    empty_board[9][26] = hidden_board[9][26]
                    empty_board[9][27] = hidden_board[9][27]
                    empty_board[9][28] = hidden_board[9][28]
                    empty_board[9][29] = hidden_board[9][29]
                    empty_board[10][26] = hidden_board[10][26]
                    empty_board[10][27] = hidden_board[10][27]
                    empty_board[10][28] = hidden_board[10][28]
                    empty_board[10][29] = hidden_board[10][29]
                    empty_board[11][26] = hidden_board[11][26]
                    empty_board[11][27] = hidden_board[11][27]
                    empty_board[11][28] = hidden_board[11][28]
                    empty_board[11][29] = hidden_board[11][29]
                    empty_board[12][26] = hidden_board[12][26]
                    empty_board[12][27] = hidden_board[12][27]
                    empty_board[12][28] = hidden_board[12][28]
                    empty_board[12][29] = hidden_board[12][29]
                    empty_board[13][27] = hidden_board[13][27]
                    empty_board[13][28] = hidden_board[13][28]
                    empty_board[13][29] = hidden_board[13][29]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif 4 <= row <= 5 and 30 <= column <= 31:
                    empty_board[2][28] = hidden_board[2][28]
                    empty_board[2][29] = hidden_board[2][29]
                    empty_board[2][30] = hidden_board[2][30]
                    empty_board[3][28] = hidden_board[3][28]
                    empty_board[3][29] = hidden_board[3][29]
                    empty_board[3][30] = hidden_board[3][30]
                    empty_board[4][28] = hidden_board[4][28]
                    empty_board[4][29] = hidden_board[4][29]
                    empty_board[4][30] = hidden_board[4][30]
                    empty_board[5][28] = hidden_board[5][28]
                    empty_board[5][29] = hidden_board[5][29]
                    empty_board[5][30] = hidden_board[5][30]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                elif (row == 15 and column == 1) or (row == 16 and 1 <= column <= 4):
                    empty_board[13][0] = hidden_board[13][0]
                    empty_board[13][1] = hidden_board[13][1]
                    empty_board[14][0] = hidden_board[14][0]
                    empty_board[14][1] = hidden_board[14][1]
                    empty_board[14][2] = hidden_board[14][2]
                    empty_board[14][3] = hidden_board[14][3]
                    empty_board[14][4] = hidden_board[14][4]
                    empty_board[15][0] = hidden_board[15][0]
                    empty_board[15][1] = hidden_board[15][1]
                    empty_board[15][2] = hidden_board[15][2]
                    empty_board[15][3] = hidden_board[15][3]
                    empty_board[15][4] = hidden_board[15][4]
                    display_board(empty_board)
                    clear_screen()
                    return 1
                else:
                    # The following else is triggered when the chosen cell is a number because we've already ruled out that it's not a bomb and if it wasn't triggered in the previous elif statements, it must be a number
                    empty_board[row-1][column-1] = hidden_board[row-1][column-1]
                    display_board(empty_board)
                    clear_screen()
                    return 1
            else:
                # The following else is triggered when the chosen cell is a bomb
                empty_board[row-1][column-1] = hidden_board[row-1][column-1]
                clear_screen()
                print('YOU LOST\n')
                display_board(empty_board)
                return 2
        else:
            clear_screen()
            print('\nREPEATED VALUES')
            return 1
    else:
        clear_screen()
        print('\nOUT OF RANGE VALUES')
        return 1

def clear_screen():
    """Function that clears the screen regardless of the operating system the code is running on"""
    if os.name == 'nt':
        os.system('cls') # Windows
    else: # 'posix'
        os.system('clear') # Mac/Linux

# Run the main function
main()
