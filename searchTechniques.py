from collections import deque
import time

TOTAL_M = 3
TOTAL_C = 3


class State:

    def __init__(self, m, c, boat, parent=None):
        self.m = m
        self.c = c
        self.boat = boat
        self.parent = parent

    def is_goal(self):
        return self.m == 0 and self.c == 0 and self.boat == 0

    def is_valid(self):

        m_right = TOTAL_M - self.m
        c_right = TOTAL_C - self.c

        if self.m < 0 or self.c < 0 or self.m > TOTAL_M or self.c > TOTAL_C:
            return False

        if self.m > 0 and self.m < self.c:
            return False

        if m_right > 0 and m_right < c_right:
            return False

        return True

    def __repr__(self):
        side = "Left" if self.boat == 1 else "Right"
        return f"(M={self.m}, C={self.c}, Boat={side})"


moves = [
    (1,0),
    (2,0),
    (0,1),
    (0,2),
    (1,1)
]


def get_successors(state):

    successors = []

    for m,c in moves:

        if state.boat == 1:
            new_state = State(state.m - m, state.c - c, 0, state)
        else:
            new_state = State(state.m + m, state.c + c, 1, state)

        if new_state.is_valid():
            successors.append(new_state)

    return successors


def reconstruct_path(state):

    path = []

    while state:
        path.append(state)
        state = state.parent

    return path[::-1]


# ---------------- BFS ----------------

def bfs(start):

    visited=set()
    queue=deque([start])
    nodes=0

    print("\nBFS Expansion Order:")

    while queue:

        state=queue.popleft()
        nodes+=1

        print(state)

        if state.is_goal():
            return reconstruct_path(state),nodes

        visited.add((state.m,state.c,state.boat))

        for s in get_successors(state):

            if (s.m,s.c,s.boat) not in visited:
                queue.append(s)

    return None,nodes


# ---------------- DFS ----------------

def dfs(start):

    visited=set()
    stack=[start]
    nodes=0

    print("\nDFS Expansion Order:")

    while stack:

        state=stack.pop()
        nodes+=1

        print(state)

        if state.is_goal():
            return reconstruct_path(state),nodes

        visited.add((state.m,state.c,state.boat))

        for s in get_successors(state):

            if (s.m,s.c,s.boat) not in visited:
                stack.append(s)

    return None,nodes


# ---------------- Depth Limited DFS ----------------

def dls(start,limit):

    stack=[(start,0)]
    visited=set()
    nodes=0

    print(f"\nDepth Limited DFS Expansion (limit={limit}):")

    while stack:

        state,depth=stack.pop()
        nodes+=1

        print(state," depth=",depth)

        if state.is_goal():
            return reconstruct_path(state),nodes

        if depth<limit:

            for s in get_successors(state):

                if (s.m,s.c,s.boat) not in visited:
                    stack.append((s,depth+1))

        visited.add((state.m,state.c,state.boat))

    return None,nodes


# ---------------- Iterative Deepening ----------------

def ids(start,max_depth):

    total_nodes=0

    for depth in range(max_depth):

        print(f"\nIDS Iteration with depth limit = {depth}")

        path,nodes=dls(start,depth)

        total_nodes+=nodes

        if path:
            return path,total_nodes

    return None,total_nodes


# ---------------- MAIN ----------------

start=State(3,3,1)

print("\n========== BFS ==========")
t=time.time()
path,n=bfs(start)
print("\nSolution Path:",path)
print("Nodes explored:",n)
print("Time:",time.time()-t)


print("\n========== DFS ==========")
t=time.time()
path,n=dfs(start)
print("\nSolution Path:",path)
print("Nodes explored:",n)
print("Time:",time.time()-t)


print("\n========== Depth Limited DFS ==========")
t=time.time()
path,n=dls(start,20)
print("\nSolution Path:",path)
print("Nodes explored:",n)
print("Time:",time.time()-t)


print("\n========== Iterative Deepening ==========")
t=time.time()
path,n=ids(start,20)
print("\nSolution Path:",path)
print("Nodes explored:",n)
print("Time:",time.time()-t)