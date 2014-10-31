class EdgeSet():
    """A basic set of edges for use with Hierholzer algorithm implementation."""
    def __init__(self):
        self.edges = set()

    def addEdge(self, v1, v2):
        if not self.__contains__((v1, v2)):
            self.edges.add((v1, v2))

    def removeEdge(self, v1, v2):
        self.edges.discard((v1, v2))
        self.edges.discard((v2, v1))

    def isEmpty(self):
        return len(self.edges) == 0

    def __contains__(self, anotherEdge):
        """ Allows us to check if the edge is already accounted for in the set. """
        for edge in self.edges:
            if edge[0] == anotherEdge[0] and edge[1] == anotherEdge[1]:
                return True
            if edge[0] == anotherEdge[1] and edge[1] == anotherEdge[0]:
                return True
        return False
