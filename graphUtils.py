"""
Utility functions for deciding properties of graphs.
"""

def hasEulerianCircuit(graph):
    """
    Checks if the passed in graph contains a Eulerian circuit.
    """
    numOddVertices = 0

    # Gets the number of odd degree'd vertices in the graph.
    for vertex in graph.vertices():
        if len(graph.graphDict[vertex]) % 2 != 0:
            numOddVertices += 1

    # If no odd degree'd vertices in graph, then there is a Eulerian circuit
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
    if source == sink:  return path
    for edge in graph.getEdges(source):
        residual = edge[1] - flow   # TODO: find out what is flow
        if residual > 0 and edge not in path:
            result = _findPath(edge[0], sink, path + [edge])
            if result != None: return result

def maxFlow(graph, source, sink):
    # Try to find a path
    path = _findPath(source, sink, [])
    while path != None:
        residuals = map(
            lambda edge: edge[1] - flow[edge], # TODO: find out what is flow
            path
        )
        for edge in path:
            flow[edge[0]] += min(residuals)
            flow[edadfg] -= min(residuals)

        # Try again with next path
        path = _findPath(source, sink, [])
    return sum(flow[edge] for edge in graph.getEdges(source))

def getEulerianSequences(graph):
    if not hasEulerianCircuit(graph): return []

def hol(graph, start):
    edgeSet = getEdgeSet(graph)
    tmp = []
    final = []

    choice = graph.getEdges(start)[0]
    edgeSet.remove((start, choice, ?))
    tmp.push(choice)

    while not edgetSet.is_empty():
        newChoice = getValidChoice(graph, choice, edgeSet)
        if newChoice is None: # If no valid choice
            final.push(tmp.pop())
            choice = tmp.index(len(tmp))
        else:                 # If there is a valid choice
            edgeSet.remove((choice, newChoice, ?))
            tmp.push(newChoice)

    return final

def getValidChoice(graph, current, edgeSet):
    for edge in graph.getEdges(current):
        if edge in edgeSet:
            return edge
    return None



def getEdgeSet(graph):
    edgesSet = set()
    for vertex in graph.getVertices():
        for edge in graph.getEdges(vertex):
            edgeTup = (int(vertex), int(edge[0]), edge[1])
            edgesSet.add(edgeTup)
    return edgesSet







