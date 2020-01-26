# Sudoku solver
A modestly fast Sudoku solver implemented in Python.

This solver is optimized to solve the puzzle using a depth first search that tries to reduce the branching factor at every level as far as possible. Depending on the hardware, approximate solve times are below 0.05 seconds for most puzzles, with the hardest ones taking below 1 second (but these are very rare). The program can also determine that a given puzzle is unsolvable in a similar amount of time.

The provided executable file will allow you to run the program in command prompt without a python installation. It can be found under releases in v1.0, Solver 1.

To use the solver, run the program and input each row of the Sudoku grid line by line, using any non-numerical character (or 0) as a placeholder for blank spaces. You do not have to fill in the whole row, only fill up to the last number provided in that row (the program will assume that the rest of the row is blank). The program will then check that the grid entered is valid (valid does not mean solvable) before attempting to solve it. If a solution is found, the solution will be printed, along with the time that it took to solve it.

If you find any bugs or have any suggestions for improvement, please send me an email at hc.hu@utoronto.ca. I value all feedback!

Sample run of the program:
```
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
*9*|*1*|8**
713|*59|*2*
***|3*2|**9
---+---+---
427|***|***
**9|***|2**
***|***|487
---+---+---
9**|5*8|***
*3*|29*|748
**2|*4*|*5*
Solving...

Solved!

Solution:
295|614|873
713|859|624
648|372|519
---+---+---
427|186|395
859|437|261
361|925|487
---+---+---
974|568|132
536|291|748
182|743|956

Solved in 0.014966726303100586 seconds.

Would you like to solve another puzzle? (enter 'y' to try again)
Input response here: n

Process finished with exit code 0
```

[Will update this with technical details in the future.]