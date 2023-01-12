#You have a strongly connected directed graph that has positive weights in the adjacency matrix g. The graph is represented as a square matrix, where g[i][j] is the weight of the edge (i, j), or -1 if there is no such edge.
#Given g and the index of a start vertex s, find the minimal distances between the start vertex s and each of the vertices of the graph.
#Example
#For
#g = [[-1, 3, 2],
#     [2, -1, 0],
#     [-1, 0, -1]]
#and s = 0, the output should be
#graphdistances(g, s) = [0, 2, 2].
#The distance from the start vertex 0 to itself is 0.
#The distance from the start vertex 0 to vertex 1 is 2 + 0 = 2.
#The distance from the start vertex 0 to vertex 2 is 2.
#Input/Output
#[time limit] 4000ms (py)
#[input] array.array.integer g
#The given graph in the form of an adjacency matrix. If g[i][j] = -1, then there is no edge between vertices i and j. Otherwise, g[i][j] is the weight of the edge between vertices i and j.
#Constraints:
#1 ≤ g.length ≤ 100,
#g[i].length = g.length,
#-1 ≤ g[i][j] ≤ 300.
#[input] integer s
#The index of the start vertex (0-based).
#Constraints:
#0 ≤ s < g.length.
#[output] array.integer
#An array of minimal distances from the start vertex to each of the vertices of the graph.
from heapq import heappush, heappop

def graphdistances(g, s):
    # Initialize the distances to infinity
    distances = [float('inf')] * len(g)
    # Set the distance to the start vertex to 0
    distances[s] = 0
    # Initialize a priority queue to store the unvisited vertices
    queue = []
    # Add the start vertex to the queue
    heappush(queue, (0, s))
    # Initialize a dictionary to store the distances and vertices
    d = {s: 0}
    # Initialize a set to store the visited vertices
    visited = set()
    # While the queue is not empty
    while queue:
        # Pop the vertex with the smallest distance
        distance, vertex = heappop(queue)
        # Skip the vertex if it has already been visited
        if vertex in visited:
            continue
        # Mark the vertex as visited
        visited.add(vertex)
        # Update the distances of the adjacent vertices
        for v, w in enumerate(g[vertex]):
            if w != -1:
                new_distance = distance + w
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    d[v] = new_distance
                    heappush(queue, (new_distance, v))
    # Return the distances
    return distances


g = [[-1, 3, 2],
        [2, -1, 0],
        [-1, 0, -1]]
s = 0
print(graphdistances(g, s))
