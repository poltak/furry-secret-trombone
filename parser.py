import re
import sys
from graph import Graph

# Regex patterns to match valid input files
NUM_PATTERN = r"\d+"
E_NODES_PATTERN = r"\d+, \d+"
NETWORK_EDGE_PATTERN = r"(\d+ \d+|\d+)"
LIST_ENTRIES_PATTERN = r"(G|T|C|A)"

def _parseNumber(line):
    """
    Parses all lines in task 1 and 2 graphs format files that contain single numbers.
    :return: int containing value found on specific line in input file.
    """
    match = re.findall(NUM_PATTERN, line)
    return int(match[0])

def _buildEdges(numEdges, fileObj):
    """
    Parses the e_nodes list in task 1 graphs format file.
    :return: dict containing all the edges their capacities in KVP format 'v1' : [('v2', capacity), ...]
    """
    graph = Graph()

    line = fileObj.readline()
    while line != "];\n":
        pairs = []
        found = re.findall(E_NODES_PATTERN, line)
        #for pair in found:
        #    pairs.append([digit for digit in re.findall(NUM_PATTERN, pair)])
        pairs = map((lambda pair: tuple(map(int, re.findall(NUM_PATTERN, pair)))), found)

        map(graph.addEdgey, pairs)

        line = fileObj.readline()
    return graph

def parseTaskOne(filePath):
    graph = Graph()
    with open(filePath, 'r') as fileObj:
        numEdges = _parseNumber(fileObj.readline())
        numNodes = _parseNumber(fileObj.readline())
        graph = _buildEdges(numEdges, fileObj)
        print graph

def main(filePath):
    parseTaskOne(filePath)

if __name__ == '__main__':
    main(sys.argv[1])

