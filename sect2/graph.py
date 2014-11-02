class FlowGraph(object):
    """
    Main data structure to represent the flow network graph. Contains representations for both the underlying directed
    graph, and a complementary data structure representing the flow for each edge.
    """
    def __init__(self):
        self.origGraph = {}
        self.edgeFlow = {}

    def addVertex(self, vertex):
        self.origGraph[vertex] = []

    def getEdges(self, vertex):
        """
        Returns the list of outgoing edges from the given vertex.
        """
        return self.origGraph[vertex]

    def addEdges(self, v1, v2, capacity = 0):
        """
        Adds new edges between vertices v1, v2, both in the original graph and residual graph.
        """
        if v1 == v2:  return
        if v1 not in self.origGraph: self.addVertex(v1)
        if v2 not in self.origGraph: self.addVertex(v2)

        edge = Edge(v1, v2, capacity)
        reverseEdge = Edge(v2, v1, 0)

        # Make links from both edges to each other
        edge.addReverseEdge(reverseEdge)
        reverseEdge.addReverseEdge(edge)

        # Set up the edges in the graph
        self.origGraph[v1].append(edge)

        # Set up the flows in the edge flow dictionary
        self.edgeFlow[edge] = 0
        self.edgeFlow[edge.reverseEdge] = 0

    def updateEdgeFlow(self, edge, newValue):
        """
        Given a new value, add it to the flow on given edge, and remove it from the reverse edge.
        """
        self.edgeFlow[edge] += newValue
        self.edgeFlow[edge.reverseEdge] -=newValue

class Edge(object):
    """
    A simple data structure to represent an edge between two vertices.
    Also holds a pointer to the reverse edge, as each directed each will have the reverse edge in the residual graph.
    """
    def __init__(self, v1, v2, capacity = 0):
        self.source = v1
        self.sink = v2
        self.capacity = capacity
        self.reverseEdge = None

    def addReverseEdge(self, reverseEdge):
        self.reverseEdge = reverseEdge

    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)
