import sys
import re
from collections import namedtuple
from graph import FlowGraph


NUM_PATTERN = r"\d+"

def _parseNumber(line):
    """
    Parses all lines in task 1 and 2 graphs format files that contain numbers.
    :return: int containing value found on specific line in input file.
    """
    match = re.findall(NUM_PATTERN, line)
    return int(match[0])

def createFlowGraph(filePath):
    """
    Parses properly formatted input file and returns a flow graph create based on that input.
    """
    graph = FlowGraph()
    try:
        fileObj = open(filePath, 'r')
        numNodes = _parseNumber(fileObj.readline())
        numEdges = _parseNumber(fileObj.readline())     # Not used

        # Set all the edges as specified in input file
        for line in fileObj:
            edge = map(int, re.findall(NUM_PATTERN, line))
            graph.addEdges(edge[0], edge[1], edge[2])

        # Return both the graph object and sequence
        GraphInfo = namedtuple('GraphInfo', ['graph', 'numNodes'])
        return GraphInfo(graph=graph, numNodes=numNodes)
    except IOError:
        print 'Error opening file %s' % filePath
        sys.exit(1)