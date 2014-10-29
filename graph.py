from operator import concat

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

    # return: '0 : [4->0, 5->0, 6->1]'
    def __str__(self):
        neighboursList = ['\n\t%2d (capacity:%2d)' % (neighbour.key, self.getCapacityBetweenNeighbour(neighbour)) for neighbour in self.adjacentVertices]
        returnString = '\nvertex %d:\t' % self.key
        for neighbourStr in neighboursList:
            returnString += neighbourStr
        return returnString + '\n'


class Graph(object):
    def __init__(self):
        self.vertices = {}

    def addVertex(self, key):
        self.vertices[key] = _Vertex(key)

    def addEdge(self, v1, v2, capacity = 0):
        if v1 not in self:  self.addVertex(v1)
        if v2 not in self:  self.addVertex(v2)
        self.vertices[v1].addNeighbour(self.vertices[v2], capacity)
        self.vertices[v2].addNeighbour(self.vertices[v1], capacity)

    def addEdgey(self, pair, capacity = 0):
        self.addEdge(pair[0], pair[1], capacity)


    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, vertex):
        return vertex in iter(self.vertices)

    def __str__(self):
        returnString = ''
        for vertex in self.vertices.values():
            returnString += str(vertex)
        return returnString
