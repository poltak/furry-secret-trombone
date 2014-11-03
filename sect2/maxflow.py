"""
This file contains my actual implementation of the Ford-Fulkerson max flow algorithm.
"""
from graph import Edge

def _findPathNonRec(graph, source, goal):
    """
    Essentially implements a non-recursive DFS to find paths from the source to the goal in a given graph.
    NOT USED BY DEFAULT- Incomplete, doesn't work on larger graphs
    """
    # Set up the stack with first edge
    stack = [(Edge(source, source), [])]
    currentPath = []
    tmpEdge = stack[0][0]

    while stack:
        (vertex, path) = stack.pop()
        if vertex.sink == goal: # Base case
            yield path
        for edge in [edges for edges in graph.getEdges(vertex.sink) if edges not in path]:
            tmpEdge = edge
            currentPath = path
            residual = edge.capacity - graph.edgeFlow[edge]
            if residual > 0 and edge not in path:
                stack.append((edge, path[:] + [edge]))

def _findPathRec(graph, source, goal, path):
    """
    Essentially implements a recursive DFS to find a path form the source to the goal
    Doesn't work on larger graphs due to Python limitations on call stack overflow.
    """
    if(source == goal): # Base case
        return path
    for edge in graph.getEdges(source):
        residual = edge.capacity - graph.edgeFlow[edge]
        if residual > 0:
            if (edge not in path and edge.reverseEdge not in path):
                toVertex = edge.sink
                resultCompare = path
                result = _findPathRec(graph, toVertex, goal, path[:] + [edge])

                if result != None:
                    # Only add edge to path if it's not a dead-end
                    if resultCompare == result + [edge]:
                        path.append(edge)
                    return result


def maxFlow(graph, source, sink):
    """
    Calculates max flow in a graph from the source to sink vertices. Uses the Ford-Fulkerson algorithm.
    """

    # # # BELOW IS THE RECURSIVE IMPLEMENTATION CALL # # #
    path = _findPathRec(graph, source, sink, [])
    while path != None:
        residuals = map(lambda edge: (edge.capacity - graph.edgeFlow[edge]), path)

        # For all the edges in found path, update them with the min val of all residuals
        map(lambda edge: graph.updateEdgeFlow(edge, min(residuals)), path)
        path = _findPathRec(graph, source, sink, [] )

    # # # BELOW IS THE NON-RECURSIVE IMPLEMENTATION CALL # # #
    """
    paths = _findPathNonRec(graph, source, sink)
    for path in paths:
        residuals = map(lambda edge: (edge.capacity - graph.edgeFlow[edge]), path)

        # For all the edges in found path, update them with the min val of all residuals
        map(lambda edge: graph.updateEdgeFlow(edge, min(residuals)), path)
    """
    return sum(graph.edgeFlow[edge] for edge in graph.getEdges(source))
