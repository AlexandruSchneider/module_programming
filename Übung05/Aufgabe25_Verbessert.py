"""
Author: Alexandru Schneider
Datum: 21. 10. 2021
Programmiersprache: Python 3.8.8
Aufgabe 25 - Sudoku

# Rules for Sudoku:
# 1. Needs at least 17 numbers already filled in
# 2. Only from 1 to 9 in horizontal line, each number only once
# 3. Only from 1 to 9 in vertical line, each number only once
# 4. In each 3x3 square numbers only from 1 to 9, each number only once
"""
import time

# If no grid is given for solving Sudoku this one is used
gridDefault = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
               [4, 5, 6, 7, 8, 9, 1, 2, 3],
               [7, 8, 9, 1, 2, 3, 4, 5, 6],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Checks for rule 1 by iterating through every value from left to right, top to bottom
def checkNumberOfValues(grid):
    counter = 0
    for row in grid:
        for value in row:
            if value != 0:
                counter += 1
    if counter >= 17:
        return True
    return False


# Checks for rule 2 by setting the row and iterating through all the values in the row and checking for duplicates
def checkValueInRow(grid, row, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    return True


# Checks for rule 3 (same principle as in checkValueInRow)
def checkValueInCol(grid, col, num):
    for x in range(9):
        if grid[x][col] == num:
            return False
    return True


# Checks for rule 4 by rounding downwards to 0, 3 or 6 and then checking all the values in that box
def checkValueInBox(grid, row, col, num):
    # get the start row of a 3x3 box
    startRow = row - row % 3

    # get the start col of a 3x3 box
    startCol = col - col % 3

    # Checks every Value in the 3x3 box with the input (duplicate check)
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


# checks the rules defined at the beginning
# returns the methods above (ALL of them have to be true to proceed, since no rules should be broken)
def checkRules(grid, row, col, num):
    return checkValueInRow(grid, row, num) and checkValueInCol(grid, col, num) and checkValueInBox(grid, row, col, num)


def Suduko(grid, row=0, col=0):

    # Check if last value is reached (bottom right corner)
    if row == 8 and col == 9:
        return True

    # Reset at the end of "line" --> next row and reset col to 0
    if col == 9:
        row += 1
        col = 0

    # Search for empty Value (0)
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)

    # If value is 0 then try all possibilities
    for num in range(1, 10):

        # Check if the possible Value is in the rules
        if checkRules(grid, row, col, num):

            # Set at the empty position to possible correct value
            grid[row][col] = num

            # start process again
            if Suduko(grid, row, col + 1):

                # return True --> Value has been found
                return True

        # If the set Value is not in the rules then return until value is in the rules
        grid[row][col] = 0

    # if you come to the last position but didnt return true before, then sudoku is unsolvable
    return False

def solveSudoku(grid=gridDefault, row=0, col=0, make=False):
    # If a Sudoku should be made, then set make, true and the sudoku can be empty (and have multiple solutions)
    if not make and not checkNumberOfValues(grid):
        return False

    # If a Sudoku isn't possible to begin with
    if not checkRules(grid, row, col, grid[row][col]) and grid[row][col] != 0:
        return False

    return Sudoku(grid, row, col)

gridTestingSolvable = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
                       [0, 1, 0, 0, 0, 4, 0, 0, 0],
                       [4, 0, 7, 0, 0, 0, 2, 0, 8],
                       [0, 0, 5, 2, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 9, 8, 1, 0, 0],
                       [0, 4, 0, 0, 0, 3, 0, 0, 0],
                       [0, 0, 0, 3, 6, 0, 0, 7, 2],
                       [0, 7, 0, 0, 0, 0, 0, 0, 3],
                       [9, 0, 3, 0, 0, 0, 6, 0, 4]]

gridMakeing = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# Prints the Values as a Sudoku
def printSudoku(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(str(grid[i][j]), end=" ")
        print("")


startTime = time.time()
if solveSudoku(gridTestingSolvable):
    endTime = time.time()
    printSudoku(gridTestingSolvable)
    print(f"Suduko has been solved in {round(endTime - startTime, 5)} seconds")
else:
    print("Solution does not exist:(")
