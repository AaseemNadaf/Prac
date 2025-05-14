from collections import defaultdict, deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()
        traversal.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal

# Example usage
if __name__ == "__main__":
    graph = defaultdict(list)
    edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]

    for u, v in edges:
        graph[u].append(v)

    for v in graph:
        print("Vertex " + str(v) + " is connected to: " + str(graph[v]))

    for start in [2, 0]:
        print("\nBFS starting from vertex " + str(start) + ":")
        print(" -> ".join(map(str, bfs(graph, start))))


"""
Time Complexity: O(V + E)

Space Complexity: O(V)

Where:

V is the number of vertices in the graph.

E is the number of edges.
"""