graph = {
    'S': {'A': 3, 'B': 5},
    'A': {'S': 3, 'D': 3, 'B': 4},
    'D': {'A': 3, 'G': 5},
    'G': {'D': 5},
    'B': {'S': 5, 'A': 4, 'C': 4},
    'C': {'B': 4, 'E': 6},
    'E': {'C': 6}
}

def explore_all_paths(graph, source, destination, current_path, visited):
    visited[source] = True
    current_path.append(source)

    if source == destination:
        print(' -> '.join(current_path))
    else:
        dead_end = True
        for neighbor, cost in sorted(graph[source].items(), key=lambda x: x[1]):
            if not visited[neighbor]:
                dead_end = False
                explore_all_paths(graph, neighbor, destination, current_path, visited)

        if dead_end:
            print(' -> '.join(current_path + ["(Dead End)"]))

    current_path.pop()
    visited[source] = False

def find_all_paths(graph, source, destination):
    print(f"All paths from {source} to {destination}:")
    visited = {node: False for node in graph}
    current_path = []
    explore_all_paths(graph, source, destination, current_path, visited)

source = 'S'
destination = 'G'

find_all_paths(graph, source, destination)
