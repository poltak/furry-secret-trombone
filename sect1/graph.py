class Graph(object):
    """
    Basic Graph ADT using adjacency lists for each vertex
    """
    def __init__(self):
        self.vertices = dict()      # Dictionary of vertices to sets of vertices (adjacency list style)

    def addVertex(self, key):
        self.vertices[key] = set()

    def _addEdge(self, v1, v2, capacity = 0):
        """
        Adds a single directed edge from v1 to v2 with specified capacity (call twice for bidirectional edge).
        """
        if v1 not in self:  self.addVertex(v1)
        if v2 not in self:  self.addVertex(v2)
        self.vertices[v1].add((v2, capacity))

    def addUndirectedEdge(self, args):
        """
        A hacky addEdge wrapper that allows creating undirected edge.
        """
        self._addEdge(int(args[0]), int(args[1]), args[2])
        self._addEdge(int(args[1]), int(args[0]), args[2])

    def getVertices(self):
        return self.vertices.keys()

    def getEdges(self, vertex):
        try:
            return self.vertices[vertex]
        except KeyError:
            return []

    def alterEdgeCapacity(self, v1, v2, change):
        for edge in self.vertices[v1]:
            if edge[0] == v2:
                edge[1] += change
                break

    def getVertexDegree(self, vertex):
        return len(self.getEdges(vertex))

    def getEdgeLabel(self, v1, v2):
        for edge in self.getEdges(v1):
            if edge[0] == v2:   return edge[1]
        return None

    def __contains__(self, vertex):
        return vertex in iter(self.vertices)

    def __str__(self):
        """
        Returns string representation of the graph.
        """
        retStr = ''
        for item in self.vertices.items():
            retStr += 'vertex %s\n' % str(item[0])
            for neighbour in item[1]:
                retStr += '\t%s (label/capacity: %s)\n' % (str(neighbour[0]), str(neighbour[1]))
        return retStr
