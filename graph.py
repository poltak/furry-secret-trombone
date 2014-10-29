class _Vertex(object):
    def __init__(self, key):
        self.key = key
        self.adjacentVertices = {}

    def addNeighbour(self, neighbour, capacity = 0):
        self.adjacentVertices[neighbour] = capacity

    def getNeighbours(self):
        return self.adjacentVertices.keys()

    def getCapacityBetweenNeighbour(self, neighbour):
        return self.adjacentVertices[neighbour]

    def __str__(self):
        """
        Returns string representation of the vertex (trust me, it does).
        """
        return '\nvertex %2d:\t' % self.key + ''.join(map(
            lambda neighbour: '\n\t%2d (capacity:%2d)' % (neighbour.key, self.getCapacityBetweenNeighbour(neighbour)),
            self.adjacentVertices
        )) + '\n'


class Graph(object):
    def __init__(self):
        self.vertices = {}      # Dictionary of vertices (adjacency list style)

    def addVertex(self, key):
        self.vertices[key] = _Vertex(key)

    def addEdge(self, v1, v2, capacity = 0):
        if v1 not in self:  self.addVertex(v1)
        if v2 not in self:  self.addVertex(v2)
        self.vertices[v1].addNeighbour(self.vertices[v2], capacity)
        self.vertices[v2].addNeighbour(self.vertices[v1], capacity)

    def addEdgeHacky(self, args):
        """
        Hacky addEdge method to fit into the functional programming style of my parser, as I have no idea how OO Python works...
        """
        if len(args) == 3:
            self.addEdge(args[0], args[1], args[2])
        elif len(args) == 2:
            self.addEdge(args[0], args[1])

    def getVertices(self):
        return self.vertices.keys()

    def __contains__(self, vertex):
        return vertex in iter(self.vertices)

    def __str__(self):
        """
        Returns string representation of the graph.
        """
        return ''.join(map(str, self.vertices.values()))
