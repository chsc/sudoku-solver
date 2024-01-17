#!/usr/bin/python3

# Simple Sudoku Solver

def _num_to_set(i):
    return {1, 2, 3, 4, 5, 6, 7, 8, 9} if i == 0 else {i}

def _convert_to_grid(board):
    return [[_num_to_set(i) for i in l] for l in board]

def _first_in_set(s):
    for e in s:
        break
    return e
    
def _is_single_element_set(e):
    return len(e) == 1

def _remove_from_set(s, e):
    if e in s:
        s.remove(e)
        return True
    return False

def _set_to_str(s):
    return str(_first_in_set(s)) if _is_single_element_set(s) else "_"

class Solver:
    def __init__(self, grid):
        self.grid = grid

    def _eliminate3x3(self, i, j):
        ci, cj = i // 3, j // 3
        oi, oj = ci * 3, cj * 3
        c = self.grid[i][j]
        if _is_single_element_set(c):
            return False
        changed = False
        for ii in range(oi, oi + 3):
            for jj in range(oj, oj + 3):
                if ii == i and jj == j:
                    continue
                e = self.grid[ii][jj]
                if _is_single_element_set(e):
                    chg = _remove_from_set(c, _first_in_set(e))
                    changed = changed or chg
        return changed
    
    def _eliminate1x9(self, i, j):
        c = self.grid[i][j]
        if _is_single_element_set(c):
            return False
        changed = False
        for jj in range(9):
            if jj == j:
                continue
            e = self.grid[i][jj]
            if _is_single_element_set(e):
                chg = _remove_from_set(c, _first_in_set(e))
                changed = changed or chg
        return changed
    
    def _eliminate9x1(self, i, j):
        c = self.grid[i][j]
        if _is_single_element_set(c):
            return False
        changed = False
        for ii in range(9):
            if ii == i:
                continue
            e = self.grid[ii][j]
            if _is_single_element_set(e):
                chg = _remove_from_set(c, _first_in_set(e))
                changed = changed or chg
        return changed
    
    def _eliminate_step(self):
        changed = False
        for i in range(9):
            for j in range(9):
                chg3x3 = self._eliminate3x3(i, j)
                chg1x9 = self._eliminate1x9(i, j)
                chg9x1 = self._eliminate9x1(i, j)
                changed = changed or chg3x3 or chg1x9 or chg9x1
        return changed
    
    def _eliminate(self):
        while self._eliminate_step(): pass

    def _board_instance(self, i, j, e):
        new_grid = [[s.copy() for s in l] for l in self.grid]
        new_grid[i][j] = e
        return new_grid
    
    def _instances(self):
        for i in range(9):
            for j in range(9):
                c = self.grid[i][j]
                if not _is_single_element_set(c):
                    for v in c:
                        yield Solver(self._board_instance(i, j, {v}))

    def is_solved(self):
        for l in self.grid:
            for i in l:
                if not _is_single_element_set(i):
                    return False
        return True
    
    def solve(self, d = 2):
        self._eliminate()
        if self.is_solved():
            print("Result:")
            self.print()
            return True
        if d == 0:
            return False
        for i in self._instances():
            if i.solve(d - 1):
                return True
        return False
    
    def print(self):
        for l in self.grid:
            sline = " ".join([_set_to_str(j) for j in l])
            print(sline)

def solve(board):
    s = Solver(_convert_to_grid(board))
    print("Start:")
    s.print()
    s.solve()
    
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
 
board_easy = [
    [0, 8, 0, 4, 0, 2, 9, 0, 5],
    [0, 7, 0, 9, 0, 0, 8, 0, 0],
    [1, 0, 4, 3, 8, 0, 0, 0, 0],
    [8, 0, 0, 0, 1, 0, 0, 3, 0],
    [6, 4, 3, 0, 0, 0, 1, 5, 2],
    [0, 2, 0, 0, 5, 0, 0, 0, 7],
    [0, 0, 0, 0, 2, 6, 3, 0, 4],
    [0, 0, 9, 0, 0, 7, 0, 6, 0],
    [4, 0, 5, 1, 0, 9, 0, 7, 0]
]

board_medium = [
    [0, 3, 0, 1, 0, 5, 0, 6, 0],
    [9, 1, 0, 0, 0, 0, 0, 8, 5],
    [0, 0, 7, 0, 2, 0, 1, 0, 0],
    [2, 8, 0, 0, 0, 0, 0, 5, 3],
    [0, 0, 0, 2, 0, 6, 0, 0, 0],
    [4, 5, 0, 0, 0, 0, 0, 1, 7],
    [0, 0, 5, 0, 8, 0, 3, 0, 0],
    [6, 4, 0, 0, 0, 0, 0, 7, 9],
    [0, 9, 0, 7, 0, 1, 0, 2, 0]
]

board_hard = [
    [5, 0, 3, 0, 0, 0, 0, 9, 2],
    [0, 0, 0, 4, 0, 6, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 4, 0, 0, 2, 0, 0, 6],
    [0, 8, 6, 0, 0, 0, 2, 5, 0],
    [2, 0, 0, 8, 0, 0, 3, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 7, 0, 5, 0, 0, 0],
    [9, 2, 0, 0, 0, 0, 5, 0, 3]
]

board_hell = [
    [0, 0, 0, 0, 0, 2, 0, 7, 4],
    [3, 0, 0, 0, 6, 0, 2, 1, 0],
    [5, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 8, 0, 0],
    [0, 8, 0, 9, 0, 6, 0, 2, 0],
    [0, 0, 3, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 8],
    [0, 5, 7, 0, 1, 0, 0, 0, 9],
    [8, 1, 0, 3, 0, 0, 0, 0, 0]
]

solve(board)
solve(board_easy)
solve(board_medium)
solve(board_hard)
solve(board_hell)
