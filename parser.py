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
LIST_ENTRIES_PATTERN = r"(G|T|C|A)"


def _parseNumber(line):
    """
    Parses all lines in task 1 and 2 graphs format files that contain numbers.
    :return: int containing value found on specific line in input file.
    """
    match = re.findall(NUM_PATTERN, line)
    return int(match[0])

def buildEdges(fileObj, taskSwitch):
    """
    Switches between the two main edge building methods (task 1 and 2)
    """
    return _buildEdgesTaskOne(fileObj) if taskSwitch else _buildEdgesTaskTwo(fileObj)

def _buildEdgesTaskOne(fileObj):
    graph = Graph()

    line = fileObj.readline()
    while line != "];\n":
        pairs = []
        found = re.findall(E_NODES_PATTERN, line)
        pairs = map(
            lambda pair: map(
                int,
                re.findall(NUM_PATTERN, pair)
            ),
            found
        )
        map(graph.addEdgeHacky, pairs)
        line = fileObj.readline()
    return graph

def _buildEdgesTaskTwo(fileObj):
    graph = Graph()
    eachLine = map(
        lambda line: map(
            int,
            re.findall(NUM_PATTERN, line)
        ),
        fileObj
    )
    map(graph.addEdgeHacky, eachLine)
    return graph


def main(filePath, taskSwitch):
    with open(filePath, 'r') as fileObj:
        numNodes = _parseNumber(fileObj.readline())     # Not used
        numEdges = _parseNumber(fileObj.readline())     # Not used
        graph = buildEdges(fileObj, taskSwitch)
    return graph

def usage():
    print "usage: parser.py [graph file] [1|2]"
    sys.exit(1)

if __name__ == '__main__':
    # Basic arg checking
    if len(sys.argv) != 3:
        usage()
    if sys.argv[2] == '1':      taskSwitch = True
    elif sys.argv[2] == '2':    taskSwitch = False
    else:                       usage()

    print main(sys.argv[1], taskSwitch)


