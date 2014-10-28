import re

class Graph(dict):

    def __init__(self, graphDict):
        """ Initializes a graph object """
        dict.__init__(self, "")
        self = graphDict
        print self

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.keys())

    def areAdjacent(self, v1, v2):
        """
        :return: boolean denoting whether or not v1 and v2 are neighbours
        """
        return self[v1].contains(v2) and self[v2].contains(v1)

    def getNeighbours(self, v1):
        """
        :return: returns a list of neighbours from v1 (empty if none)
        """
        try:
            return self[v1]
        except KeyError:
            return []

    def getEdges(self, v1):
        """
        :return: returns a list of edges from v1 (empty if none)
        """
        try:

        except KeyError:
            return []

    def addEdge(self, v1, v2):
        """
        Add edge from v1 to v2 if not already there.
        """
        return self[v1].add(v2) and self[v2].add(v1)

    def deleteEdge(self, v1, v2):
        """
        Delete edge between v1 and v2 if it exists.
        """
        return self[v1].remove(v2) and self[v2].remove(v1)

    def getEdgeCapacity(self, v1, v2):
        if not areAdjacent(v1, v2):
            return False
        return self[v1][indexOfV2][1]

    def setEdgeCapacity(self, v1, v2, newValue):
        if not areAdjacent(v1, v2):
            return False
        pass




    def __generateEdges(self):
        edges = []
        for vertex in self:
            for neighbour in self[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        tostring = ""
        # TODO: look at iterating over dicts
        for vertex in self.keys():
            neighbourStr = ""
            for neighbour in self[vertex]:
                neighbourStr += "\tvertex %s (capacity: %s)\n" % (neighbour[0] , neighbour[1])
            toString += "vertex %s :\nneighbouring vertices:\n%s\n" % (vertex, neighbourStr)

        return toString

