from queue import PriorityQueue

# Define the graph as an adjacency list with neighbors and edge weights
graph = {
    'S': {'A': 3, 'B': 5},
    'A': {'S': 3, 'D': 3, 'B': 4},
    'D': {'A': 3, 'G': 5},
    'G': {'D': 5},
    'B': {'S': 5, 'A': 4, 'C': 4},
    'C': {'B': 4, 'E': 6},
    'E': {'C': 6}
}

def branch_and_bound(graph, source, destination):
    priority_queue = PriorityQueue()
    priority_queue.put((0, [source]))

    while not priority_queue.empty():
        current_cost, current_path = priority_queue.get()

        current_node = current_path[-1]

        print(f"Current Path: {' -> '.join(current_path)}")
        print(f"Current Cost: {current_cost}")
        print()

        if current_node == destination:
            return current_path

        for neighbor, cost in graph[current_node].items():
            if neighbor not in current_path:
                new_cost = current_cost + cost
                new_path = current_path + [neighbor]
                priority_queue.put((new_cost, new_path))

    return None  # No path found

source = 'S'
destination = 'G'

result = branch_and_bound(graph, source, destination)

if result:
    print(f"Optimal path from {source} to {destination}: {' -> '.join(result)}")
    print(f"Optimal cost: {sum(graph[result[i]][result[i+1]] for i in range(len(result)-1))}")
else:
    print(f"No path from {source} to {destination}")
