"""
A module to test the performance of the solver by getting it to solve a set of puzzles.
Checker correctness is not checked, only the solve times are recorded.
"""

from datetime import datetime

from sudoku_solver import SudokuPuzzle, depth_first_solve, time


def test_performance(filename: str) -> None:
    """
    Gets the solver to solve puzzles from a text file, and prints the statistics.
    """
    symbol_set, times = {str(i) for i in range(1, 10)}, []
    with open(filename) as data:
        for line in data:
            line = line.strip('\n').replace('.', '*').replace('0', '*')
            symbols = [[c for c in line[i:i + 9]] for i in range(0, len(line), 9)]
            puzzle = SudokuPuzzle(9, symbols, symbol_set)
            start = time()
            solution = depth_first_solve(puzzle)
            end = time()
            times.append(end - start)
            print(f'Input puzzle:\n{puzzle}')
            print(f'\nSolved in {end - start:.4f} seconds.\n')
            print(f'{solution}\n')
    result = f'Puzzles solved: {len(times)}\n' \
        f'Total time taken: {sum(times)}\n' \
        f'Average time per puzzle: {sum(times) / len(times)}\n' \
        f'Max time: {max(times)}\n'

    with open('progress.txt', 'a') as log:
        log.write(f'{str(datetime.now())[:-7]} (File: {filename})')
        log.write('\n' + result + '\n')
    print(result)


if __name__ == '__main__':
    test_performance("puzzles.txt")
    test_performance("euler_sudokus.txt")
    test_performance("hardest.txt")
