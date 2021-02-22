"""
A module that tests the performance of the solver by getting it to solve a set of puzzles.
Solver correctness is not checked, only the solve times are recorded.
"""

from time import time
from datetime import datetime

from sudoku_solver import SudokuPuzzle, depth_first_solve


def measure_cpu_speed(num: int) -> float:
    """
    Estimates the average CPU speed by measuring how fast the CPU can count.
    """

    def _measure() -> int:
        count = 0
        start = time()
        while time() - start < 1:
            count += 1
        return count

    return sum(_measure() for _ in range(num)) / num


def test_performance(filename: str) -> None:
    """
    Gets the solver to solve puzzles from a text file, and prints the statistics.
    """
    symbol_set, times = {str(i) for i in range(1, 10)}, []
    speed_begin = measure_cpu_speed(5)
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
    speed_end = measure_cpu_speed(5)
    unstable = max(speed_begin, speed_end) / min(speed_begin, speed_end) > 1.10
    average_solve_time = sum(times) / len(times)
    result = f'Puzzles solved: {len(times)}\n' \
             f'Total time taken: {sum(times)}\n' \
             f'Average time per puzzle: {average_solve_time}\n' \
             f'Max time: {max(times)}\n' \
             f'Processor speeds: {speed_begin, speed_end} ({"unstable" if unstable else "stable"})\n' \
             f'Relative performance: {(speed_begin / 100_000) / (1 / average_solve_time)}\n'

    with open('progress.txt', 'a') as log:
        log.write(f'{str(datetime.now())[:-7]} (File: {filename})')
        log.write('\n' + result + '\n')
    print(result)


if __name__ == '__main__':
    test_performance("test_files/puzzles.txt")
    test_performance("test_files/euler_sudokus.txt")
    test_performance("test_files/hardest.txt")
