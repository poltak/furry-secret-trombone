import re
import sys
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

def createSectOneGraph(filePath):
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
        return graph
    except IOError:
        print 'Error opening file %s' % filePath
        sys.exit(1)

def createSectTwoGraph(filePath):
    try:
        fileObj = open(filePath, 'r')
        numNodes = _parseNumber(fileObj.readline())     # Not used
        numEdges = _parseNumber(fileObj.readline())     # Not used

        graph = Graph()
        # Set all the edges as specified in input file
        map(graph.addDirectedEdge, map(
            lambda line: map(
                int,
                re.findall(NUM_PATTERN, line)
            ),
            fileObj
        ))
        return graph
    except IOError:
        print 'Error opening file %s' % filePath
        sys.exit(1)

def main(filePath, taskOneSwitch):
    graph = createSectOneGraph(filePath) if taskOneSwitch else createSectTwoGraph(filePath)
    print graph

def usage():
    print "usage: parser.py [graph file] [1|2]"
    sys.exit(1)

if __name__ == '__main__':
    # Basic arg checking
    if len(sys.argv) != 3:      usage()

    if sys.argv[2] == '1':      taskOneSwitch = True
    elif sys.argv[2] == '2':    taskOneSwitch = False
    else:                       usage()

    main(sys.argv[1], taskOneSwitch)


