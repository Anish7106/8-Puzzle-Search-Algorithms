def bfs(start, goal):
    queue = [(start, [])]
    visited = [start]
    nodes = 0

    while queue:
        state, path = queue.pop(0)
        nodes += 1

        if state == goal:
            return path, nodes

        zero = state.index(0)
        row = zero // 3
        col = zero % 3

        moves = [
            (-1, 0, "up"),
            (1, 0, "down"),
            (0, -1, "left"),
            (0, 1, "right")
        ]

        for dr, dc, move in moves:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_zero = new_row * 3 + new_col
                new_state = list(state)
                new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.append(new_state)
                    queue.append((new_state, path + [move]))

    return None, nodes


start = []
print("Enter initial state:")
for i in range(3):
    start += list(map(int, input().split()))
start = tuple(start)

goal = []
print("Enter goal state:")
for i in range(3):
    goal += list(map(int, input().split()))
goal = tuple(goal)

path, nodes = bfs(start, goal)

print("Algorithm: BFS")
print("Path to goal:", path)
print("Number of moves:", len(path) if path else -1)
print("Nodes expanded:", nodes)
