"""
This file contains my actual implementation of the Ford-Fulkerson max flow algorithm.
"""
from graph import Edge
import time

def _findPath(graph, source, goal):
    """
    Essentially implements a non-recursive DFS to find paths from the source to the goal in a given graph.
    """
    # Set up the stack with first edge
    stack = [(Edge(source, source), [])]

    while stack:
        (currentEdge, path) = stack.pop()
        # For each edge from current vertex (ignore those edges already taken)
        for edge in [edges for edges in graph.getEdges(currentEdge.sink) if edges not in path]:
            if edge.sink == goal:
                path += [edge]
                yield path      # Return the currently found path and continue
            else:
                path += [edge]
                stack.append((edge, path))


def maxFlow(graph, source, sink):
    """
    Calculates max flow in a graph from the source to sink vertices. Uses the Ford-Fulkerson algorithm.
    """
    paths = _findPath(graph, source, sink)
    for path in paths:
        residuals = map(lambda edge: (edge.capacity - graph.edgeFlow[edge]), path)

        # For all the edges in found path, update them with the min val of all residuals
        map(lambda edge: graph.updateEdgeFlow(edge, min(residuals)), path)

    return sum(graph.edgeFlow[edge] for edge in graph.getEdges(source))
