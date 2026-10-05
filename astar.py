def manhattan(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            row = i // 3
            col = i % 3
            position = goal.index(state[i])
            goal_row = position // 3
            goal_col = position % 3
            distance += abs(row - goal_row)
            distance += abs(col - goal_col)

    return distance


def astar(start, goal):
    queue = [(manhattan(start, goal), 0, start, [])]
    visited = []
    nodes = 0

    while queue:
        queue.sort()
        f, cost, state, path = queue.pop(0)
        nodes += 1

        if state == goal:
            return path, nodes

        if state in visited:
            continue

        visited.append(state)

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
                    new_cost = cost + 1
                    h = manhattan(new_state, goal)
                    f = new_cost + h
                    queue.append((f, new_cost, new_state, path + [move]))

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

path, nodes = astar(start, goal)

print("Algorithm: A*")
print("Path to goal:", path)
print("Number of moves:", len(path) if path else -1)
print("Nodes expanded:", nodes)
