# N-Queens Problem Solver

This program solves the N-Queens problem using a hill climbing algorithm. Value method calculates the number of queen pairs that are in a conflict.
Best method checks all possible moves for each queen that would result the fewest conflicts. Move method updates board and calculates new conflicts.
After approximately 32 queens, my program has a hard time computing the best solution.

## Here is an example with N=4:

### Initial Board:
Q _ _ _ <br>
_ _ _ Q <br>
_ Q _ _ <br>
_ _ Q _ <br>
### Initial Conflicts: 1

and here is the solved Board:

### Final Board:
_ Q _ _ <br>
_ _ _ Q <br>
Q _ _ _ <br>
_ _ Q _ <br>
### Final Conflicts: 0

## Another example when N=8:

### Initial Board:
_ _ _ _ Q _ _ _ <br>
_ _ _ _ _ _ _ Q <br>
Q _ _ _ _ _ _ _ <br>
_ _ _ _ _ _ Q _ <br>
_ Q _ _ _ _ _ _ <br>
_ _ _ _ _ Q _ _ <br>
_ _ Q _ _ _ _ _ <br>
_ _ _ Q _ _ _ _ <br>
### Initial Conflicts: 3

### Final Board:
_ _ _ _ Q _ _ _ <br>
_ _ Q _ _ _ _ _ <br>
Q _ _ _ _ _ _ _ <br>
_ _ _ _ _ Q _ _ <br>
_ _ _ _ _ _ _ Q <br>
_ Q _ _ _ _ _ _ <br>
_ _ _ Q _ _ _ _ <br>
_ _ _ _ _ _ Q _ <br>
### Final Conflicts: 0