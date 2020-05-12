# Sudoku solver
A modestly fast Sudoku solver implemented in Python.

This solver is optimized to solve the puzzle using a depth first search that tries to reduce the branching factor at every level as far as possible. Depending on the hardware, approximate solve times are below 0.05 seconds for most puzzles, with the hardest ones taking below 1 second (but these are very rare). The program can also determine that a given puzzle is unsolvable in a similar amount of time.

The provided executable file will allow you to run the program in command prompt without a python installation. It can be found under releases in v1.1, Solver exe.

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
### Pushing the boundaries
This solver can *theoretically* solve any *n* x *n* puzzle (where *n* is a perfect square). But because the general problem of solving Sudoku puzzles is known to be [NP-complete](https://en.wikipedia.org/wiki/NP-completeness "Wikipedia: NP-completeness"), this means that the time taken to solve progressively larger puzzles increases very rapidly.

Here is a sample of the program trying to solve an empty 16 x 16 puzzle:
```
* * * * | * * * * | * * * * | * * * *
* * * * | * * * * | * * * * | * * * *
* * * * | * * * * | * * * * | * * * *
* * * * | * * * * | * * * * | * * * *
--------+---------+---------+--------
* * * * | * * * * | * * * * | * * * *
* * * * | * * * * | * * * * | * * * *
* * * * | * * * * | * * * * | * * * *
* * * * | * * * * | * * * * | * * * *
--------+---------+---------+--------
* * * * | * * * * | * * * * | * * * *
* * * * | * * * * | * * * * | * * * *
* * * * | * * * * | * * * * | * * * *
* * * * | * * * * | * * * * | * * * *
--------+---------+---------+--------
* * * * | * * * * | * * * * | * * * *
* * * * | * * * * | * * * * | * * * *
* * * * | * * * * | * * * * | * * * *
* * * * | * * * * | * * * * | * * * *
Solving...

Solved!

Solution:
K E H L | B G A M | O N I F | P C D J
J M N C | H I F P | D G E L | K B O A
P O B F | E C N D | A M K J | G L H I
A G I D | L K J O | P C H B | N E M F
--------+---------+---------+--------
B A K P | O J H N | L D F E | M G I C
H F G M | I B P E | K J C N | D A L O
D N O J | F A C L | G I M P | B H K E
L I C E | D M G K | H B O A | F J P N
--------+---------+---------+--------
C P M N | K H D G | B E A O | I F J L
I K J O | M F B A | N L G H | E D C P
G H E B | C P L J | F K D I | O N A M
F L D A | N O E I | C P J M | H K G B
--------+---------+---------+--------
M J P K | A N I C | E H B G | L O F D
E C F G | P D O B | M A L K | J I N H
N D L H | J E K F | I O P C | A M B G
O B A I | G L M H | J F N D | C P E K

Solved in 9.57807970046997 seconds.
```
And then a 25 x 25 one...
```
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
----------+-----------+-----------+-----------+----------
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
----------+-----------+-----------+-----------+----------
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
----------+-----------+-----------+-----------+----------
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
----------+-----------+-----------+-----------+----------
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
* * * * * | * * * * * | * * * * * | * * * * * | * * * * *
Solving...

Solved!

Solution:
I O T N P | M G W F C | X H B D Y | J R Q U E | L K A V S
K J E C S | Q U H B V | A P L O G | W F T Y X | I D R M N
Y R X F L | D N A J T | M S U W V | K B O I G | P C E Q H
Q H W A U | Y P O S K | F N R I E | V L D C M | B G T J X
V D G B M | I L R X E | Q J K C T | A N H S P | U Y F W O
----------+-----------+-----------+-----------+----------
M K L T O | J V B W X | S U P Q A | D H Y E R | F I G N C
R A H S F | P T Y D Q | L V N J I | C O G K U | X E W B M
B Y I E W | U C N R F | T M D G H | L S X A Q | K V P O J
G X N P Q | K A M O H | C Y F E B | I T W J V | R S U L D
D C V U J | E I S L G | K O W R X | F P B M N | Q A H Y T
----------+-----------+-----------+-----------+----------
W P O M T | X B K E I | H Q A L F | G V S R Y | D J N C U
U B S G E | C R L M J | V D T P W | N A K O I | Y X Q H F
X F J I D | A Q V T N | G C Y K U | E W M B H | S L O P R
H L R Y A | W D U P O | N I J B S | Q X C F T | G M V E K
N Q C V K | F H G Y S | E R O X M | P U L D J | W B I T A
----------+-----------+-----------+-----------+----------
J G F K R | O Y X H P | D B V A N | T M I W C | E Q S U L
S V Q L Y | B J T N W | U K I M C | X E A P F | O H D R G
C M D W I | V S Q A U | R E H Y P | O G N L K | J T X F B
E T P X B | R F C I M | O G Q S L | U Y J H D | N W K A V
A N U O H | G E D K L | W T X F J | B Q R V S | M P C I Y
----------+-----------+-----------+-----------+----------
F U K D N | T X J C B | Y A E V O | M I P G W | H R L S Q
L E A J G | H W P Q R | B X M T K | S C F N O | V U Y D I
T I M H C | L O F G Y | P W S U Q | R D V X B | A N J K E
O W Y Q V | S M I U D | J L G N R | H K E T A | C F B X P
P S B R X | N K E V A | I F C H D | Y J U Q L | T O M G W

Solved in 209.4494128227234 seconds.
```
Of course, since the 16 x 16 and 25 x 25 puzzles started with an empty grid, this is not so much *solving* a puzzle as simply finding one of the *countably infinite* solutions. For the sake of my computer, and due to the lack of characters in the English alphabet, I've decided not to go further than this.
