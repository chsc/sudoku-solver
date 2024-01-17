# Sudoku Solver

This is a simple Sudoku solver algorithm implemented in Python, based on elimination and backtracking techniques.

## Algorithm Overview

The Sudoku solver utilizes two main techniques: elimination and backtracking.

1. Elimination
The elimination technique involves iteratively eliminating possible values for each cell based on the values present in its row, column, and 3x3 subgrid. The algorithm scans through the Sudoku grid and eliminates possibilities until no further eliminations can be made.

2. Backtracking
If the elimination technique alone does not solve the Sudoku, the algorithm employs backtracking. Backtracking is a recursive approach where the solver makes a guess for a cell, continues solving, and if a contradiction is encountered, it backtracks and tries a different guess. This process continues until a solution is found or all possibilities are exhausted.

## Usage

Clone the repository:

    git clone https://github.com/chsc/sudoku-solver.git

Navigate to the project directory:

    cd sudoku-solver

Run the solver:

    python sudoku_solver.py

## Example
To solve a Sudoku puzzle, input the initial board configuration in the sudoku_solver.py file. For example:

    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    solve(board)

Example output:

    Start:
    5 3 _ _ 7 _ _ _ _
    6 _ _ 1 9 5 _ _ _
    _ 9 8 _ _ _ _ 6 _
    8 _ _ _ 6 _ _ _ 3
    4 _ _ 8 _ 3 _ _ 1
    7 _ _ _ 2 _ _ _ 6
    _ 6 _ _ _ _ 2 8 _
    _ _ _ 4 1 9 _ _ 5
    _ _ _ _ 8 _ _ 7 9
    Result:
    5 3 4 6 7 8 9 1 2
    6 7 2 1 9 5 3 4 8
    1 9 8 3 4 2 5 6 7
    8 5 9 7 6 1 4 2 3
    4 2 6 8 5 3 7 9 1
    7 1 3 9 2 4 8 5 6
    9 6 1 5 3 7 2 8 4
    2 8 7 4 1 9 6 3 5
    3 4 5 2 8 6 1 7 9

The solve function will attempt to solve the puzzle and display the solution.

Feel free to adapt the code to integrate it into your own projects or modify it according to your needs.