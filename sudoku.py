from pprint import pprint

# finds the next row, col on the puzzle that's not filled yet
# returns None, None if there is none


def find_next_empty(puzzle):

    # first empty space you get, return the (row, col) val of that
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    # if no spaces in the puzzle are empty, returning None, None
    return None, None

# figures out whether the guess at that row or col of the puzzle is valid
# returns True if valid, False otherwise


def is_valid(puzzle, guess, row, col):

    # checking if row is valid by making sure the guess is not in the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # checking if the column is valid by making sure the guess is not in the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # getting where the 3x3 square starts
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    # iterate over the 3 values in the row/col of that 3x3 square
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # if all checks pass, return True
    return True

# mutates the puzzle to be the solution, but only if the solution exists
# returns True if solution exists, False otherwise


def solve_sudoku(puzzle):

    # choosing somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # if there are no empty spots left, then we are done
    if row is None:
        return True

    # if there is a spot to put a number, then make a guess between 1 and 9
    # trying all of the numbers until we find a combination that works
    for guess in range(1, 10):

        # checking if this guess is a valid one in terms of the rules
        if is_valid(puzzle, guess, row, col):
            # if valid, then it goes on that spot in the puzzle
            puzzle[row][col] = guess

            # recursively calling the function to solve the puzzle
            if solve_sudoku(puzzle):
                return True

        # if the guess we chose doesn't solve the puzzle or the guess is not valid, then
        #   we need to backtrack and try another new number,
        # we are resetting the guess in that spot to be empty
        puzzle[row][col] = -1

    # if no number works, then this puzzle is unsolveable and False is returned
    return False


if __name__ == '__main__':
    example_board = [[3, 9, -1, -1, 5, -1, -1, -1, -1],
                     [-1, -1, -1, 2, -1, -1, -1, -1, 5],
                     [-1, -1, -1, 7, 1, 9, -1, 8, -1],
                     [-1, 5, -1, -1, 6, 8, -1, -1, -1],
                     [2, -1, 6, -1, -1, 3, -1, -1, -1],
                     [-1, -1, -1, -1, -1, -1, -1, -1, 4],
                     [5, -1, -1, -1, -1, -1, -1, -1, -1],
                     [6, 7, -1, 1, -1, 5, -1, 4, -1],
                     [1, -1, 9, -1, -1, -1, 2, -1, -1]]
    print(solve_sudoku(example_board))
    pprint(example_board)
