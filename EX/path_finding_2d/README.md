This project explores the performance of three different pathfinding
algorithms on 2D maps with different sizes.

The algorithms tested are Breadth-First Search (BFS), Greedy search, A* search.

Conclusion

BFS took the longest time in all three scenrarios, but found the shortest path.
Greedy search was the fastest algorithm but took the most number of iterations.
A* showed balanced performance between speed and optimality.
So if you want shortest path, use BFS or A*, if you want fastest, then choose Greedy.


Here is some data:
Testing on SMALL map...
Running BFS...
Time taken: 0.4909687042236328
Iterations: 555
Path length: 554
------
Running Greedy Search...
Time taken: 0.04799818992614746
Iterations: 983
Path length: 982
------
Running A* Search...
Time taken: 0.10699701309204102
Iterations: 555
Path length: 554
------
Testing on MEDIUM map...
Running BFS...
Time taken: 2.145970344543457
Iterations: 1248
Path length: 1247
------
Running Greedy Search...
Time taken: 0.08699774742126465
Iterations: 1974
Path length: 1973
------
Running A* Search...
Time taken: 1.0140297412872314
Iterations: 1248
Path length: 1247
------
Testing on LARGE map...
Running BFS...
Time taken: 4.811956405639648
Iterations: 1844
Path length: 1843
------
Running Greedy Search...
Time taken: 0.4730098247528076
Iterations: 4130
Path length: 4129
------
Running A* Search...
Time taken: 1.3519957065582275
Iterations: 1844
Path length: 1843
------
