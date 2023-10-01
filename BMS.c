#include <stdio.h>
#include <stdbool.h>

#define MAX_VERTICES 100

char adjacencyList[MAX_VERTICES][MAX_VERTICES];
int adjacencyListSize[MAX_VERTICES];
bool visited[MAX_VERTICES];

void initGraph() {
    for (int i = 0; i < MAX_VERTICES; i++) {
        adjacencyListSize[i] = 0;
        visited[i] = false;
    }
}

void addEdge(char src, char dest) {
    int srcIndex = src - 'A';
    int destIndex = dest - 'A';
    
    adjacencyList[srcIndex][adjacencyListSize[srcIndex]++] = dest;
    adjacencyList[destIndex][adjacencyListSize[destIndex]++] = src;
}

void printPathsUtil(char src, char dest, char path[], int pathLength) {
    int srcIndex = src - 'A';
    
    visited[srcIndex] = true;
    path[pathLength] = src;
    pathLength++;

    if (src == dest) {
        for (int i = 0; i < pathLength; i++) {
            printf("%c ", path[i]);
        }
        printf("\n");
    } else {
        for (int i = 0; i < adjacencyListSize[srcIndex]; i++) {
            int neighborIndex = adjacencyList[srcIndex][i] - 'A';
            if (!visited[neighborIndex]) {
                printPathsUtil(adjacencyList[srcIndex][i], dest, path, pathLength);
            }
        }
    }

    visited[srcIndex] = false; // Reset the visited flag for backtracking
}

void printAllPaths(char src, char dest) {
    char path[MAX_VERTICES];
    int pathLength = 0;
    printPathsUtil(src, dest, path, pathLength);
}

int main() {
    initGraph();

    // Add edges to the graph
    addEdge('S', 'A');
    addEdge('A', 'D');
    addEdge('D', 'G');
    addEdge('A', 'B');
    addEdge('B', 'C');
    addEdge('C', 'E');
    addEdge('S', 'B');

    char source = 'S';
    char destination = 'G';

    printf("All possible paths from %c to %c:\n", source, destination);
    printAllPaths(source, destination);

    return 0;
}
