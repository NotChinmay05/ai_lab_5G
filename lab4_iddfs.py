def dls(start, goal, depth, graph, visited_order):
    visited_order.append(start)

    if start == goal:
        return True

    if depth <= 0:
        return False

    for child in graph.get(start, []):
        if dls(child, goal, depth - 1, graph, visited_order):
            return True

    return False


def iddfs(start, end_depth, goal, graph):
    depth = 0
    while depth <= end_depth:
        visited_order = []
        result = dls(start, goal, depth, graph, visited_order)
        
        print(f"Depth {depth} traversal: {' -> '.join(visited_order)}")

        if result:
            print("Goal Found")
            return True

        depth += 1

    print("Goal Not Found within depth limit")
    return False


graph = {}
n = int(input("Enter the number of nodes in the tree: "))

print("Enter node and its children separated by space (e.g., A B C). Leave children blank if leaf node:")
for _ in range(n):
    data = input().split()
    node = data[0]
    children = data[1:]
    graph[node] = children

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
max_depth = int(input("Enter the maximum depth limit (end): "))

print("\n--- IDDFS Traversal ---")
iddfs(start_node, max_depth, goal_node, graph)
