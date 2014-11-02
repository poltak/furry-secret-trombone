"""
Utility functions for deciding properties of graphs.
"""
from edgeset import EdgeSet

def getEulerianCircuits(graph):
    """
    Returns a list of all possible Eulerian circuits for a given graph.
    If graph has none, it returns an empty list.
    """
    if not _hasEulerianCircuit(graph): return []

    # Find the Euler circuits starting from all vertices in the graph
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
    for vertex in range(len(path)-1):
       labels += graph.getEdgeLabel(path[vertex], path[vertex+1])
    return labels

def longestCommonSubstring(seq, foundSeq):
    """
    Given two strings, finds the longest common substring.
    """
    substr = ''
    for i in range(len(seq)):
        for j in range(len(seq)-i+1):
            if j > len(substr) and seq[i:i+j] in foundSeq:
                substr = seq[i:i+j]
    return substr

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
