"""
Utility functions for deciding properties of graphs.
"""
from edgeset import EdgeSet

def maxFlow(origGraph, flowGraph, source, sink):
    # Try to find a path
    path = _findPath(source, sink, [])
    while path != None:
        residuals = map(
            lambda edge: edge[1] - flowGraph[edge], # TODO: find out what is flow
            path
        )
        for edge in path:
            flow[edge[0]] += min(residuals)
            flow[edadfg] -= min(residuals)

        # Try again with next path
        path = _findPath(source, sink, [])
    return sum(flow[edge] for edge in graph.getEdges(source))

def _findPath(graph, source, sink, path):
    if source == sink:  return path
    for edge in graph.getEdges(source):
        residual = edge[1] - flow   # TODO: find out what is flow
        if residual > 0 and edge not in path:
            result = _findPath(edge[0], sink, path + [edge])
            if result != None: return result

def getEulerianCircuits(graph):
    """
    Returns a list of all possible Eulerian circuits for a given graph.
    If graph has none, it returns an empty list.
    """
    if not _hasEulerianCircuit(graph): return []
    eulerCircuits = []
    for vertex in graph.getVertices():
        circuit = _hierholzer(graph, vertex)
        eulerCircuits.append(circuit)

    # Reversed circuits are also valid circuits
    reversedCircuits = []
    for circuit in eulerCircuits:
        reversedCircuits.append(circuit[::-1])

    return eulerCircuits + reversedCircuits

def getLabelsForPath(graph, path):
    """
    Given a path in a graph, returns a string containing all the labels on that path.
    """
    labels = ''
    for vertex in range(0, len(path) -1):
       labels += graph.getEdgeLabel(path[vertex], path[vertex+1])
    return labels

# TODO
def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

# TODO
def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

def _hasEulerianCircuit(graph):
    """
    Checks if the passed in graph contains a Eulerian circuit.
    """
    # Gets the number of odd degree'd vertices in the graph.
    for vertex in graph.getVertices():
        if graph.getVertexDegree(vertex) % 2 != 0:
            return False
    # If no odd degree'd vertices in graph, then there is a Eulerian circuit
    return True

def _hierholzer(graph, start):
    """
    Performs Hierholzer's algorithm to get a Eulerian circuit from a graph.
    """
    edgeSet = _generateEdgeSet(graph)
    tmpStack = []
    finalPathStack = []

    # Set up start point
    choice = _getValidChoice(graph, start, edgeSet)
    edgeSet.removeEdge(start, choice)
    tmpStack.append(choice)

    # Keep choosing next vertex, to generate Eulerian circuit
    while not edgeSet.isEmpty():
        newChoice = _getValidChoice(graph, choice, edgeSet)

        # Check if there is a valid choice from the current vertex
        if newChoice is None:   # If no valid choice can be made (backtrack)
            finalPathStack.append(tmpStack.pop())
            choice = tmpStack[-1] # Backtrack to last vertex (on top of tmp stack)
        else:                   # If there is a valid choice, go with it
            edgeSet.removeEdge(choice, newChoice)
            tmpStack.append(newChoice)
            choice = newChoice

    # All edges have been covered by this point, so pop the tmp stack's contents to the final stack
    while len(tmpStack) > 0:
        finalPathStack.append(tmpStack.pop())
    finalPathStack.append(start)

    return finalPathStack

def _getValidChoice(graph, current, edgeSet):
    """
    Returns the first valid vertex choice from the current vertex, as per
    Hierholzer's algorithm.
    Returns None if no valid choice can be made.
    """
    for edge in graph.getEdges(current):
        if (current, edge[0]) in edgeSet:
            return edge[0]
    return None

def _generateEdgeSet(graph):
    edgeSet = EdgeSet()
    for vertex in graph.getVertices():
        for edge in graph.getEdges(vertex):
            edgeSet.addEdge(vertex, edge[0])
    return edgeSet
