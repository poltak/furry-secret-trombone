def has_euclidean_circuit(graph):
    """
    Checks if the passed graph contains a Euclidean circuit.
    """
    # Get number of ODD vertices
    num_odd_vertices = 0
    for vertex in graph.vertices():
        if len(graph.graph_dict[vertex]) % 2 != 0:
            num_odd_vertices += 1

    return num_odd_vertices == 0


def _is_bipartite(graph, current_vertex, visited, colour):
    for neighbour in graph[current_vertex]:
        if not visited[int(neighbour)]:
            visited[int(neighbour)] = True
            # set neighbour to be opposite colour to prev vertex
            colour[int(neighbour)] = not colour[int(current_vertex)]
            return self._is_bipartite(graph, neighbour, visited, colour)
        # if prev colour same as current colour
        elif colour[int(neighbour)] is colour[int(current_vertex)]:
            return False
    return True


def is_bipartite(graph):
    """
    Checks if the passed graph is a bipartite graph.
    """
    start = graph.vertices()[0]
    visited = [False] * len(graph.keys())
    colour = [None] * len(graph.keys())
    visited[int(start)] = True
    colour[int(start)] = True

    return self._is_bipartite(graph, start, visited, colour)

