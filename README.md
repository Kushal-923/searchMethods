# Uninformed Search Algorithms

This project implements several **Uninformed Search Strategies** using the classic **Missionaries and Cannibals Problem**.

## Author

Kushal Pandey

---

# Problem Description

There are:

- 3 Missionaries
- 3 Cannibals
- One boat (capacity = 2)

Rules:

- If cannibals outnumber missionaries on any side, missionaries are eaten.
- The boat can carry at most 2 people.

Goal:

Move all missionaries and cannibals from the **left bank to the right bank safely**.

---

# Implemented Algorithms

1. Breadth First Search (BFS)
2. Depth First Search (DFS)
3. Depth-Limited Search (DLS)
4. Iterative Deepening Search (IDS)

Each algorithm prints:

- Intermediate states
- Final solution path
- Nodes explored
- Execution time

---

# Running the Program

python search_algorithms.py

---

# Output Example

BFS Expansion Order:
(M=3, C=3, Boat=Left)
(M=3, C=1, Boat=Right)
...

Solution Path:
(3,3,L) → (3,1,R) → ...

Nodes explored: 15

---

# Comparison of Algorithms

| Algorithm | Optimal | Memory Usage |
|--------|--------|--------|
| BFS | Yes | High |
| DFS | No | Low |
| DLS | Depends on limit | Low |
| IDS | Yes | Moderate |

---

# Concepts Demonstrated

- State Space Search
- Uninformed Search Strategies
- Problem Representation in AI