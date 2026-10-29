# 8-Puzzle Search Algorithms

A small Python project that solves the 8-puzzle with four classic search strategies and prints the solution path and number of explored nodes.

## The puzzle

Example start:

| 1 | 2 | 3 |
| --- | --- | --- |
| 4 | _ | 6 |
| 7 | 5 | 8 |

Goal:

| 1 | 2 | 3 |
| --- | --- | --- |
| 4 | 5 | 6 |
| 7 | 8 | _ |

The blank is represented by `0` when entering a board.

## Algorithms

| Script | Strategy |
| --- | --- |
| `bfs.py` | Breadth-First Search |
| `dfs.py` | Depth-limited Depth-First Search |
| `astar.py` | A* with Manhattan Distance |
| `ucs.py` | Uniform Cost Search |

## Run

Requires Python 3. No external packages are needed.

```bash
python bfs.py
python dfs.py
python astar.py
python ucs.py
```

Each script prompts for the initial board and goal board as three rows of numbers. For DFS, enter a maximum search depth when prompted.

Example input:

```text
Initial state:
1 2 3
4 0 6
7 5 8

Goal state:
1 2 3
4 5 6
7 8 0
```

For this example, the solution is `down, right` (2 moves).

## What it reports

Each solver prints the path to the goal, the number of moves, and the number of nodes expanded.

**Author:** Anish Bandaru
