# branch and bound + heuristic
from queue import PriorityQueue

# Define the graph as an adjacency list with neighbors and heuristic values
graph = {
    'S': {'A': 3, 'B': 5},
    'A': {'S': 3, 'D': 3, 'B': 4},
    'D': {'A': 3, 'G': 5},
    'G': {'D': 5},
    'B': {'S': 5, 'A': 4, 'C': 4},
    'C': {'B': 4, 'E': 6},
    'E': {'C': 6}
}

heuristic = {'S': 10, 'A': 7, 'D': 5, 'G': 0, 'B': 6, 'C': 7, 'E': 7}

def branch_and_bound_heuristic(graph, heuristic, source, destination):
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic[source], [source]))

    visited = set()

    while not priority_queue.empty():
        _, current_path = priority_queue.get()

        current_node = current_path[-1]

        if current_node in visited:
            continue

        visited.add(current_node)

        print(f"Current Path: {' -> '.join(current_path)}")
        print()

        if current_node == destination:
            return current_path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                new_path = current_path + [neighbor]
                priority_queue.put((heuristic[neighbor], new_path))

    return None  # No path found

source = 'S'
destination = 'G'

result = branch_and_bound_heuristic(graph, heuristic, source, destination)

if result:
    print(f"Optimal path from {source} to {destination}: {' -> '.join(result)}")
else:
    print(f"No path from {source} to {destination}")
