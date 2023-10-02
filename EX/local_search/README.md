# N-Queens Problem Solver

This program solves the N-Queens problem using a hill climbing algorithm.

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