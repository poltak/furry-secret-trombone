class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v
        self.capacity = w
    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)

class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def get_edges(self, v):
        return self.adj[v]

    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w)
        redge = Edge(v,u,0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0

    def find_path(self, source, sink, path):
        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_path( edge.sink, sink, path + [edge])
                if result != None:
                    return result

    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))


NUM_PATTERN = r"\d+"
E_NODES_PATTERN = r"\d+, \d+"
NETWORK_EDGE_PATTERN = r"(\d+ \d+|\d+)"
SEQ_PATTERN = r"(G|T|C|A)"
import re
def _parseNumber(line):
    """
    Parses all lines in task 1 and 2 graphs format files that contain numbers.
    :return: int containing value found on specific line in input file.
    """
    match = re.findall(NUM_PATTERN, line)
    return int(match[0])

import sys
def main():
    g = FlowNetwork()
    sys.setrecursionlimit(10000000)
    try:
        fileObj = open(sys.argv[1], 'r')
        numNodes = _parseNumber(fileObj.readline())     # Not used
        numEdges = _parseNumber(fileObj.readline())     # Not used

        # Set all the edges as specified in input file
        for v in range(0, 1000):
            g.add_vertex(v)
        for line in fileObj:
            edge = map(int, re.findall(NUM_PATTERN, line))
            g.add_edge(edge[0], edge[1], edge[2])
        print str(g.max_flow(0, 999))



    except IOError:
        print 'Error opening file %s' % filePath
        sys.exit(1)

if __name__ == '__main__':
    main()