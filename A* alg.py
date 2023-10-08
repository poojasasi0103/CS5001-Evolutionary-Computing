import heapq

def a_star_search(graph, start, goal, heuristic):
    open_list = [(0 + heuristic[start], 0, [start])]  # (f_cost, g_cost, path)
    closed_set = set()

    while open_list:
        _, current_cost, current_path = heapq.heappop(open_list)
        current_node = current_path[-1]

        print(f"Current Path: {' -> '.join(current_path)}")
        print(f"Current Cost: {current_cost}")
        print()

        if current_node == goal:
            return current_path

        if current_node in closed_set:
            continue

        closed_set.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor not in closed_set:
                new_g_cost = current_cost + cost
                new_f_cost = new_g_cost + heuristic[neighbor]
                new_path = current_path + [neighbor]
                heapq.heappush(open_list, (new_f_cost, new_g_cost, new_path))

    return None  # No path found

# Test the A* algorithm
start_node = 'S'
goal_node = 'G'
result_path = a_star_search(graph, start_node, goal_node, heuristic)

if result_path:
    print(f"Optimal path from {start_node} to {goal_node}: {' -> '.join(result_path)}")
    print(f"Optimal cost: {sum(graph[result_path[i]][result_path[i+1]] for i in range(len(result_path)-1))}")
else:
    print(f"No path from {start_node} to {goal_node}")
