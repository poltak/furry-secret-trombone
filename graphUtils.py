"""
Utility functions for deciding properties of graphs.
"""

def hasEuclideanCircuit(graph):
    """
    Checks if the passed in graph contains a Euclidean circuit.
    """
    numOddVertices = 0

    # Gets the number of odd degree'd vertices in the graph.
    for vertex in graph.vertices():
        if len(graph.graphDict[vertex]) % 2 != 0:
            numOddVertices += 1

    # If no odd degree'd vertices in graph, then there is a Euclidean circuit
    return numOddVertices == 0


def _isBipartite(graph, currentVertex, visited, colour):
    for neighbour in graph[currentVertex]:
        if not visited[int(neighbour)]:
            visited[int(neighbour)] = True

            # Set neighbour to be opposite colour to prev vertex
            colour[int(neighbour)] = not colour[int(currentVertex)]
            return _isBipartite(graph, neighbour, visited, colour)

        # If previous colour same as current colour
        elif colour[int(neighbour)] is colour[int(currentVertex)]:
            return False
    return True


def isBipartite(graph):
    """
    Recursively checks if the passed in graph is a bipartite graph using colouring.
    """

    # Get a start vertex
    start = graph.vertices()[0]

    visited = [False] * len(graph.keys())
    colour = [None] * len(graph.keys())
    visited[int(start)] = True
    colour[int(start)] = True

    return _isBipartite(graph, start, visited, colour)

def _findPath(graph, source, sink, path):
    if source == sink:
        return path
    for edge in graph.getEdges(source):
        residual = edge


def maxFlow(graph):
    pass



