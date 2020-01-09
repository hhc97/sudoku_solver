# sudoku-solver
A modestly fast Sudoku solver implemented in Python.

This solver is highly optimized and will solve the puzzle using a depth first solve that tries to reduce the branching factor at every level as far as possible. Depending on the hardware, approximate solve times are below 0.05 seconds for most puzzles, with the hardest ones taking below 1 second (but these are very rare). The program can also determine that a given puzzle is unsolvable in a similar amount of time.

The provided executable file will allow you to run the program in command prompt without a python installation. It can be found under releases in v1.0, Solver 1.

To use the solver, run the program and input each row of the Sudoku grid line by line, using any non-numerical character (or 0) as a placeholder for blank spaces. You do not have to fill in the whole row, only fill up to the last number provided in that row (the program will assume that the rest of the row is blank). The program will then check that the grid entered is valid (valid does not mean solvable) before attempting to solve it. If a solution is found, the solution will be printed, along with the time that it took to solve it. A sample run of the program is provided in sample_run.txt.

If you find any bugs or have any suggestions for improvement, please send me an email at hc.hu@utoronto.ca. I value all feedback!

[Will update this with technical details in the future.]