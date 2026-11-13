import heapq

goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

def manhattan(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == val:
                            distance += abs(i - x) + abs(j - y)
    return distance

def misplaced_tiles(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def solve_manhattan(start, goal):
    open_list = []
    h = manhattan(start, goal)
    heapq.heappush(open_list, (h, 0, start))
    closed = set()
    open_states = {tuple(map(tuple, start))}

    while open_list:
        f, g, current = heapq.heappop(open_list)
        curr_tuple = tuple(map(tuple, current))
        open_states.discard(curr_tuple)

        if current == goal:
            return "Solution", g

        closed.add(curr_tuple)

        for neighbor in get_neighbors(current):
            neigh_tuple = tuple(map(tuple, neighbor))
            if neigh_tuple in closed:
                continue
            ng = g + 1
            nh = manhattan(neighbor, goal)
            nf = ng + nh
            if neigh_tuple not in open_states:
                heapq.heappush(open_list, (nf, ng, neighbor))
                open_states.add(neigh_tuple)

    return "No solution", -1

def solve_misplaced(start, goal):
    pq = []
    f = misplaced_tiles(start, goal)
    heapq.heappush(pq, (f, 0, start))
    visited = set()

    while pq:
        f, g, current = heapq.heappop(pq)
        curr_tuple = tuple(map(tuple, current))
        if curr_tuple in visited:
            continue
        visited.add(curr_tuple)

        if current == goal:
            return "Solved", g

        for neighbor in get_neighbors(current):
            neigh_tuple = tuple(map(tuple, neighbor))
            if neigh_tuple not in visited:
                ng = g + 1
                nf = ng + misplaced_tiles(neighbor, goal)
                heapq.heappush(pq, (nf, ng, neighbor))

    return "No solution", -1

start_state = []
print("Enter initial state row by row (use 0 for blank):")
for _ in range(3):
    start_state.append(list(map(int, input().split())))

res_m, moves_m = solve_manhattan(start_state, goal_state)
res_mt, moves_mt = solve_misplaced(start_state, goal_state)

print(f"Manhattan Algorithm: {res_m}, Moves: {moves_m}")
print(f"Misplaced Tiles Algorithm: {res_mt}, Moves: {moves_mt}")
