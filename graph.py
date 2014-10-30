class Graph(object):
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

    def addDirectedEdge(self, args):
        """
        Hacky addEdge method to fit into the functional programming style of my parser, as I have no idea how OO Python works...
        Adds a directed edge between the args.
        """
        if len(args) == 3:
            self._addEdge(args[0], args[1], args[2])
        elif len(args) == 2:
            self._addEdge(args[0], args[1])

    def addUndirectedEdge(self, args):
        """
        Another hacky addEdge wrapper that allows creating undirected edge.
        """
        if len(args) == 3:
            self._addEdge(args[0], args[1], args[2])
            self._addEdge(args[1], args[0], args[2])
        elif len(args) == 2:
            self._addEdge(args[0], args[1])
            self._addEdge(args[1], args[0])

    def getVertices(self):
        return self.vertices.keys()

    def getEdges(self, vertex):
        return self.vertices[vertex]

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
                retStr += '\t%s (capacity: %s)\n' % (str(neighbour[0]), str(neighbour[1]))
        return retStr
