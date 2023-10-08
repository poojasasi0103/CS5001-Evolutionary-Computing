#include <stdio.h>

#define MAX_VERTICES 7

int graph[MAX_VERTICES][MAX_VERTICES];
int visited[MAX_VERTICES];
int path[MAX_VERTICES];
int pathIndex = 0;

void initGraph(int numVertices) {
    for (int i = 0; i < numVertices; ++i) {
        visited[i] = 0;
        for (int j = 0; j < numVertices; ++j) {
            graph[i][j] = 0;
        }
    }
}

void addEdge(int v, int w) {
    graph[v][w] = 1;  // Directed edge
}

void printPath(int start, int end) {
    printf("Path: ");
    for (int i = start; i <= end; ++i) {
        printf("%d ", path[i]);
    }
    printf("\n");
}

void dfs(int vertex, int goal, int numVertices) {
    visited[vertex] = 1;
    path[pathIndex++] = vertex;

    if (vertex == goal) {
        // Print the current path
        printPath(0, pathIndex - 1);
        return;  // Stop recursion when the goal is reached
    }

    for (int i = 0; i < numVertices; ++i) {
        if (graph[vertex][i] && !visited[i]) {
            dfs(i, goal, numVertices);
        }
    }

    visited[vertex] = 0;  // Reset visited for backtracking
    pathIndex--;
}

int main() {
    int numVertices = 7;

    initGraph(numVertices);

    // Adding edges for a directed graph
    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 2);
    addEdge(1, 4);
    addEdge(2, 1);
    addEdge(2, 3);
    addEdge(3, 5);
    addEdge(4, 6);

    int source = 0;
    int goal = 6;

    printf("DFS traversal from vertex %d to %d:\n", source, goal);
    dfs(source, goal, numVertices);

    return 0;
}
