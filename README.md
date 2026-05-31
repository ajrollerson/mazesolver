Readme –  Maze solver

Maze Solver is a small Python project that generates and solves random mazes using a Depth-First Search (DFS) algorithm. Built as part of a Boot.dev guided project, it was extended to support experimentation and comparison between multiple maze-solving strategies through visualisation and timing metrics.
Key skills and knowledge developed: 

•	Algorithmic design and implementation.
•	Added and managed dynamic UI elements. 
•	Integrated live timers into an existing animation loop. 
•	Added comparative visualisation between algorithms. 
•	Managed state between the Maze and Window classes.

Key features:

The guided project initially provided the following functionality:

- Maze generation and randomisation.
- A DFS maze solver algorithm.
- A small testing suite.
- 
Personal additions made that enhance the base project:

- Implemented a Directional Heuristic DFS algorithm (DH DFS), which uses direction-dependent wall checking priorities to influence traversal behaviour.
- Integrated independent timing systems into the graphical simulation, managing timer state across the Window and Maze classes to synchronise live GUI updates with algorithm execution and enable comparative performance visualisation.

Known limitations:

•	Some elements have been hardcoded for the timer and the graphical elements.
•	Testing suite is somewhat limited, and no tests currently exist to provide feedback on the functioning of the algorithms.

Design choices:

•	I chose to add two timers with their own colours onto the window and have both algorithms run on top of each other. Had considered ‘resetting’ the maze, though the scope of doing was quite large for the size of the project. By having both algorithms and timers on screen, it would provide an immediate comparison on the performance of each algorithm.

•	Initially attempted to implement a right-hand-rule heuristic. Investigation revealed that a simple wall-following approach was insufficient within the existing recursive architecture, leading to the development of the Directional Heuristic DFS approach.

•	During development of the directional heuristic solver, significant debugging was required to diagnose infinite loops and oscillation between cells. Substantial logging and tracing were used to identify problematic traversal behaviour, leading to the introduction of direction-based state to prevent oscillation and guide traversal decisions.

Observation:

•	In most trials, the DFS algorithm outperforms the DH DFS algorithm, except when the maze happens to have a path that quickly leads to the exit, with few branching paths elsewhere.

Future improvements:

•	Expand the testing suite to validate algorithm behaviour and performance.
•	Refactor the DH DFS algorithm to reduce verbosity and improve maintainability.
