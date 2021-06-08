from collections import deque


# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, N):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)


# Function to perform DFS traversal in a directed graph to find the
# complete path between source and destination vertices
def isConnected(graph, src, dest, discovered, path):
    # mark the current node as discovered
    discovered[src] = True

    # include the current node in the path
    path.append(src)

    # if destination vertex is found
    if src == dest:
        return True

    # do for every edge `src —> i`
    for i in graph.adjList[src]:

        # if `u` is not yet discovered
        if not discovered[i]:
            # return true if the destination is found
            if isConnected(graph, i, dest, discovered, path):
                return True

    # backtrack: remove the current node from the path
    path.pop()

    # return false if destination vertex is not reachable from src
    return False


if __name__ == '__main__':

    # List of graph edges as per the above diagram
    edges = [
        (0, 3), (1, 0), (1, 2), (1, 4), (2, 7), (3, 4),
        (3, 5), (4, 3), (4, 6), (5, 6), (6, 7)
    ]

    # total number of nodes in the graph (labeled from 0 to `N-1`)
    N = 8

    # build a graph from the given edges
    graph = Graph(edges, N)

    # to keep track of whether a vertex is discovered or not
    discovered = [False] * N

    # source and destination vertex
    (src, dest) = (0, 7)

    # List to store the complete path between source and destination
    path = deque()

    # perform DFS traversal from the source vertex to check the connectivity
    # and store path from the source vertex to the destination vertex
    if isConnected(graph, src, dest, discovered, path):
        print("Path exists from vertex", src, "to vertex", dest)
        print("The complete path is", list(path))
    else:
        print("No path exists between vertices", src, "and", dest)


