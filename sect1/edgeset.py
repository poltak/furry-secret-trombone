class EdgeSet(object):
    """A basic set of edges for use with Hierholzer algorithm implementation."""
    def __init__(self):
        self.edges = set()

    def addEdge(self, v1, v2):
        exists = self.getEdge(v1, v2)
        if not exists == None:
            exists.usages += 1
        else:
            self.edges.add(Edge(v1, v2))

    def removeEdge(self, v1, v2):
        exists = self.getEdge(v1, v2)
        # Only actually delete an edge if there are no more adjacent parallel edges
        if exists.usages == 1:
            self.edges.discard(exists)
        else: # If there are those edges, we just want to decrease the number
            exists.usages -= 1

        exists = self.getEdge(v2, v1)
        if exists.usages == 1:
            self.edges.discard(exists)
        else:
            exists.usages -= 1

    def isEmpty(self):
        return len(self.edges) == 0

    def getEdge(self, v1, v2):
        """ Allows us to check if the edge is already accounted for in the set. """
        for edge in self.edges:
            if edge.v1 == v1 and edge.v2 == v2:
                return edge
            if edge.v1 == v2 and edge.v2 == v1:
                return edge
        return None

    def __contains__(self, otherEdge):
        exists = self.getEdge(otherEdge[0], otherEdge[1])
        return True if exists != None else False

class Edge(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.usages = 1     # this can be increased to represent adjacent edges
