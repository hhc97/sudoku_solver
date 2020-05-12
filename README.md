# Sudoku solver
A modestly fast Sudoku solver implemented in Python.

This solver is optimized to solve the puzzle using a depth first search that tries to reduce the branching factor at every level as far as possible. Depending on the hardware, approximate solve times are below 0.05 seconds for most puzzles, with the hardest ones taking below 1 second (but these are very rare). The program can also determine that a given puzzle is unsolvable in a similar amount of time.

The provided executable file will allow you to run the program in command prompt without a python installation. It can be found under releases in v1.0, Solver 1.

To use the solver, run the program and input each row of the Sudoku grid line by line, using any non-numerical character (or 0) as a placeholder for blank spaces. You do not have to fill in the whole row, only fill up to the last number provided in that row (the program will assume that the rest of the row is blank). The program will then check that the grid entered is valid (valid does not mean solvable) before attempting to solve it. If a solution is found, the solution will be printed, along with the time that it took to solve it.

If you find any bugs or have any suggestions for improvement, please send me an email at hc.hu@utoronto.ca. I value all feedback!

Sample run of the program:
```
Welcome to Sudoku Solver v1.1 by Haocheng Hu

Please type in row 1:-9--1-8
Please type in row 2:713-59-2
Please type in row 3:---3-2--9
Please type in row 4:427
Please type in row 5:--9---2
Please type in row 6:------487
Please type in row 7:9--5-8
Please type in row 8:-3-29-748
Please type in row 9:--2-4--5

Input puzzle:
* 9 * | * 1 * | 8 * *
7 1 3 | * 5 9 | * 2 *
* * * | 3 * 2 | * * 9
------+-------+------
4 2 7 | * * * | * * *
* * 9 | * * * | 2 * *
* * * | * * * | 4 8 7
------+-------+------
9 * * | 5 * 8 | * * *
* 3 * | 2 9 * | 7 4 8
* * 2 | * 4 * | * 5 *
Solving...

Solved!

Solution:
2 9 5 | 6 1 4 | 8 7 3
7 1 3 | 8 5 9 | 6 2 4
6 4 8 | 3 7 2 | 5 1 9
------+-------+------
4 2 7 | 1 8 6 | 3 9 5
8 5 9 | 4 3 7 | 2 6 1
3 6 1 | 9 2 5 | 4 8 7
------+-------+------
9 7 4 | 5 6 8 | 1 3 2
5 3 6 | 2 9 1 | 7 4 8
1 8 2 | 7 4 3 | 9 5 6

Solved in 0.013964653015136719 seconds.

Would you like to solve another puzzle? (enter 'y' to try again)
Input response here: n

Process finished with exit code 0
```

[Will update this with technical details in the future.]