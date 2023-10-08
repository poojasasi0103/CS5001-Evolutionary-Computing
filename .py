# Define the graph as an adjacency list with neighbors
graph = {
    'S': ['A', 'B'],
    'A': ['S', 'D', 'B'],
    'D': ['A', 'G'],
    'G': ['D'],
    'B': ['S', 'A', 'C'],
    'C': ['B', 'E'],
    'E': ['C']
}

# Heuristic function estimating remaining distance (e.g., Euclidean distance)
heuristic = {'S': 10, 'A': 7, 'D': 5, 'G': 0, 'B': 6, 'C': 7, 'E': 7}

def evaluate_solution(path, heuristic):
    total_heuristic = sum(heuristic[node] for node in path)
    return total_heuristic

def beam_search_with_heuristic(graph, source, destination, beam_width, heuristic):
    queue = [[source]]  # Queue of paths
    beam = []  # Beam for storing top 'beam_width' paths

    while queue:
        current_path = queue.pop(0)
        current_node = current_path[-1]

        if current_node == destination:
            return current_path  # Goal reached

        neighbors = graph[current_node]

        for neighbor in neighbors:
            new_path = current_path + [neighbor]
            heuristic_score = heuristic[neighbor]

            if len(beam) < beam_width:
                beam.append((heuristic_score, new_path))
            elif heuristic_score < max(beam, key=lambda x: x[0])[0]:
                max_idx = max(enumerate(beam), key=lambda x: x[1][0])[0]
                beam[max_idx] = (heuristic_score, new_path)

        beam.sort(key=lambda x: x[0])

        # Print the nodes in each traversal step
        print(f"Current Beam: {[path for _, path in beam]}")

        queue.extend([path for _, path in beam])

    return None  # Goal not reached

source = 'S'
destination = 'G'
beam_width = 2  # Beam width, set to the desired value

best_solution = beam_search_with_heuristic(graph, source, destination, beam_width, heuristic)

if best_solution:
    print(f"Best path from {source} to {destination}: {' -> '.join(best_solution)}")
    #print(f"Total heuristic: {evaluate_solution(best_solution, heuristic)}")
else:
    print(f"No path from {source} to {destination}")
