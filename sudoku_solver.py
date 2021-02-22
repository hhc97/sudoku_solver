"""
Thanks to Chaodi, for providing valuable insight on some of the
methods in the class.

This module contains the class required to represent a Sudoku puzzle,
as well as the necessary functions and methods to solve it.
The code in this module is written in Python 3.7
For more information, view the README.

===== MIT License =====

Copyright (c) 2019-2021 Haocheng Hu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from __future__ import annotations

from re import sub
from time import time
from typing import Dict, List, Optional, Set, Tuple


class SudokuPuzzle:
    """
    A representation of the current state of a Sudoku puzzle.
    """

    def __init__(self, n: int, symbols: List[List[str]],
                 symbol_set: Set[str], grid_map=None) -> None:
        """
        Initializes the puzzle.

        Empty spaces are denoted by the '*' symbol, and the grid symbols
        are represented as letters or numerals.

        ===== Preconditions =====
        - n is an integer that is a perfect square
        - the given symbol_set must contain n unique symbols
        - for the puzzle to print properly, symbols should be 1 character long
        - there are n lists in symbols, and each list has n strings as elements
        """
        # ===== Private Attributes =====
        # _n: The number of rows and columns in the puzzle.
        # _symbols: A list of lists representing
        #           the current state of the puzzle.
        # _symbol_set: The set of symbols that each row, column, and subsquare
        #              must have exactly one of for this puzzle to be solved.
        # _map: A dictionary mapping each unfilled position to the possible
        #       symbols that can still be filled in at that position.
        # _set_map: A dictionary that maps the unfilled symbols for each
        #           row, column, and subsquare set to the possible positions
        #           that they could occupy within that section.

        _n: int
        _symbols: List[List[str]]
        _symbol_set: Set[str]
        _map: Dict[Tuple[int, int], Set[str]]
        _set_map: Dict[str, Dict[str, Set[Tuple[int, int]]]]

        assert n == len(symbols), 'length of symbols not equal to value of n'
        self._n, self._symbols, self._symbol_set, self._set_map \
            = n, symbols, symbol_set, {}
        if grid_map is None:
            self._map = {}
            self._populate_map()
        else:
            self._map = grid_map

    def _populate_map(self) -> None:
        # updates _map with possible symbols for each unfilled position
        for r in range(self._n):
            for c in range(self._n):
                if self._symbols[r][c] == '*':
                    subset = self._row_set(r) | self._column_set(c) | \
                             self._subsquare_set(r, c)
                    allowed_symbols = self._symbol_set - subset
                    self._map[(r, c)] = allowed_symbols

    def _populate_set_map(self) -> None:
        # updates _set_map with missing symbols for each set
        # and the positions they could possibly occupy within the set
        for r in range(self._n):
            set_name = f'row{r}'
            self._set_map[set_name] = {}
            row_set = self._row_set(r)
            missing_symbols = self._symbol_set - row_set
            for sym in missing_symbols:
                self._set_map[set_name][sym] = set()
                for key, value in self._map.items():
                    if key[0] == r and sym in value:
                        self._set_map[set_name][sym].add(key)

    def get_symbols(self) -> List[List[str]]:
        """
        Returns a copy of symbols, for use during testing.
        """
        return [row[:] for row in self._symbols]

    def __str__(self) -> str:
        """
        Returns an easily readable string representation of the current puzzle.
        """
        string_repr, n = [], round(self._n ** (1 / 2))
        div = '--' * n + ('+' + '-' + '--' * n) * (n - 2) + '+' + '--' * n
        for i in range(self._n):
            if i > 0 and i % n == 0:
                string_repr.append(div)
            row_lst = self._symbols[i][:]
            for index in range(n, self._n, n + 1):
                row_lst.insert(index, '|')
            string_repr.append(' '.join(row_lst))
        return '\n'.join(string_repr)

    def is_solved(self) -> bool:
        """
        Returns whether the current puzzle is solved.
        """
        return not any('*' in row for row in self._symbols) \
            and self._check_row_and_col() and self._check_subsquares()

    def _check_row_and_col(self) -> bool:
        # (helper for is_solved)
        # checks that all rows and columns are filled in properly
        return all(self._row_set(i) == self._symbol_set and
                   self._column_set(i) == self._symbol_set
                   for i in range(self._n))

    def _check_subsquares(self) -> bool:
        # (helper for is_solved)
        # checks that all subsquares are filled in properly
        n = round(self._n ** (1 / 2))
        return all(self._subsquare_set(r, c) == self._symbol_set
                   for r in range(0, self._n, n) for c in range(0, self._n, n))

    def extensions(self) -> List[SudokuPuzzle]:
        """
        Returns a list of SudokuPuzzle objects that have the position
        with the least number of possibilities filled in.

        This method checks for naked singles first, and if none are found,
        checks for hidden singles. Again, if none are found, it fills in the
        spot with the least number of naked/hidden possibilities.
        """
        if not self._map:
            return []
        extensions = []
        position, possible = None, self._symbol_set | {'*'}
        for pos, values in self._map.items():
            if len(values) < len(possible):
                position, possible = pos, values
        symbol, possible_positions = None, None
        if len(possible) > 1:
            self._populate_set_map()
            for d in self._set_map.values():
                for sym, positions in d.items():
                    if len(positions) < len(possible):
                        symbol, possible_positions, = sym, positions
        if symbol:
            for pos in possible_positions:
                new_symbols = [row[:] for row in self._symbols]
                new_symbols[pos[0]][pos[1]] = symbol
                new_map = self._map.copy()
                for key in self._get_positions(pos):
                    new_map[key] = self._map[key] - {symbol}
                del new_map[pos]
                extensions.append(SudokuPuzzle(self._n, new_symbols,
                                               self._symbol_set, new_map))
        else:
            for value in possible:
                new_symbols = [row[:] for row in self._symbols]
                new_symbols[position[0]][position[1]] = value
                new_map = self._map.copy()
                for key in self._get_positions(position):
                    new_map[key] = self._map[key] - {value}
                del new_map[position]
                extensions.append(SudokuPuzzle(self._n, new_symbols,
                                               self._symbol_set, new_map))
        return extensions

    def _get_positions(self, pos: tuple) -> List[Tuple[int, int]]:
        # returns the keys of sets in _map that may need to be altered
        n = round(self._n ** (1 / 2))
        return [key for key in self._map if key[0] == pos[0] or
                key[1] == pos[1] or (key[0] // n == pos[0] // n and
                                     key[1] // n == pos[1] // n)]

    def _row_set(self, r: int) -> Set[str]:
        # returns the set of symbols of row r
        return set(self._symbols[r])

    def _column_set(self, c: int) -> Set[str]:
        # returns the set of symbols of column c
        return set(row[c] for row in self._symbols)

    def _subsquare_set(self, r: int, c: int) -> Set[str]:
        # returns the set of symbols of the subsquare that [r][c] belongs to
        n, symbols = self._n, self._symbols
        ss = round(n ** (1 / 2))
        ul_row = (r // ss) * ss
        ul_col = (c // ss) * ss
        return set(symbols[ul_row + i][ul_col + j]
                   for i in range(ss) for j in range(ss))


def depth_first_solve(puzzle: SudokuPuzzle) -> Optional[SudokuPuzzle]:
    """
    An iterative depth first search to solve the puzzle.
    """
    if puzzle.is_solved():
        return puzzle
    puzzle_queue = puzzle.extensions()
    while puzzle_queue:
        curr = puzzle_queue.pop()
        if curr.is_solved():
            return curr
        puzzle_queue.extend(curr.extensions())
    return None


def is_valid_grid(lst: list, symbol_set: set) -> bool:
    """
    Returns True if this is a valid Sudoku grid.
    """
    return not any(lst[r].count(sym) > 1 or
                   [row[c] for row in lst].count(sym) > 1
                   or _sbsq_lst(r, c, lst).count(sym) > 1
                   for r in range(len(lst)) for c in range(len(lst[r]))
                   for sym in symbol_set)


def _sbsq_lst(r: int, c: int, symbols: list) -> list:
    # (helper for is_valid_grid)
    # returns the list of symbols in the subsquare containing [r][c]
    ss = round(len(symbols) ** (1 / 2))
    return [symbols[(r // ss) * ss + i][(c // ss) * ss + j]
            for i in range(ss) for j in range(ss)]


def make_9x9_sudoku_puzzle() -> SudokuPuzzle:
    """
    Takes user input to build and return a SudokuPuzzle object.
    """
    symbol_set = {str(i) for i in range(1, 10)}
    symbols = [[n for n in sub('[^1-9]', '*',
                               input(f'Please type in row {r}:')[:9].ljust(9, '*'))]
               for r in range(1, 10)]
    if is_valid_grid(symbols, symbol_set):
        return SudokuPuzzle(9, symbols, symbol_set)
    else:
        print(f'\nGrid entered:\n{SudokuPuzzle(9, symbols, symbol_set)}')
        print('\nInvalid grid entered, please retry.\n')
        return make_9x9_sudoku_puzzle()


def main() -> None:
    """
    Runs the program, which will prompt the user to input a Sudoku puzzle row by row.
    Once the input is received, it will be formatted and checked for validity.
    If it is a valid input, the program will make a SudokuPuzzle object and
    try to solve it. If there is a solution, the solution will be printed to stdout.
    """
    a = make_9x9_sudoku_puzzle()
    print(f'\nInput puzzle:\n{a}\nSolving...')
    time1 = time()
    sol = depth_first_solve(a)
    time2 = time()
    if sol:
        print('\nSolved!\n\nSolution:')
        print(sol)
        print(f'\nSolved in {time2 - time1} seconds.')
    else:
        print('No solution found :(')
    print("\nWould you like to solve another puzzle? (enter 'y' to try again)")
    retry = input('Input response here: ')
    if retry.lower() == 'y':
        print()
        main()


if __name__ == "__main__":
    print('Welcome to Sudoku Solver v1.2 by Haocheng Hu\n')
    main()
