import re
import sys
from collections import namedtuple
from graph import Graph

"""
NOTE: This script is a parser, hence it's full of hacky regex magic, and functional programming wizardry, so don't bother
reading through it, or you'll probably cry.
"""

# Regex patterns to match valid input files
NUM_PATTERN = r"\d+"
E_NODES_PATTERN = r"\d+, \d+"
NETWORK_EDGE_PATTERN = r"(\d+ \d+|\d+)"
SEQ_PATTERN = r"(G|T|C|A)"

def parseFile(filePath):
    """
    Main parsing method. Given valid file path, returns a constructed graph and sequence to find.
    """
    try:
        fileObj = open(filePath, 'r')
        numNodes = _parseNumber(fileObj.readline())
        numEdges = _parseNumber(fileObj.readline())

        # Parse file
        eNodes = ''
        line = fileObj.readline()
        while line != '];\n':
            eNodes += line
            line = fileObj.readline()
        eStart = _parseSequence(fileObj.readline())
        seq = _parseSequence(fileObj.readline())

        graph = Graph()
        # Set all the edges as specified in input file
        i = 0
        for line in re.split(r'\n', eNodes):
            for pair in re.findall(E_NODES_PATTERN, line):
                graph.addUndirectedEdge(re.findall(NUM_PATTERN, pair) + [eStart[i]])
                i += 1
            line = fileObj.readline()

        # Return both the graph object and sequence
        GraphInfo = namedtuple('GraphInfo', ['graph', 'seq'])
        return GraphInfo(graph=graph, seq=seq)
    except IOError:
        print 'Error opening file %s' % filePath
        sys.exit(1)

def _parseNumber(line):
    """
    Parses all lines in task 1 and 2 graphs format files that contain numbers.
    :return: int containing value found on specific line in input file.
    """
    match = re.findall(NUM_PATTERN, line)
    return int(match[0])

def _parseSequence(line):
    """
    Parses the lines containing the sequences, and returns them as a single string.
    """
    return ''.join(re.findall(SEQ_PATTERN, line))
