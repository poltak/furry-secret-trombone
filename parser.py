import sys
import re

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


def _parseENodes(fileObj):
    """
    Parses the e_nodes list in task 1 graphs format file.
    :return: dict containing all the edges their capacities in KVP format 'v1' : [('v2', capacity), ...]
    """
    graphDict = {}

    line = fileObj.readline()
    while line != "];\n":
        pairs = []
        found = re.findall(E_NODES_PATTERN, line)
        for pair in found:
            pairs.append([digit for digit in re.findall(NUM_PATTERN, pair)])

        for pair in pairs:
            try:
                graphDict[pair[0]].append((pair[1], 0))
            except KeyError:
                graphDict[pair[0]] = [(pair[1], 0)]

            try:
                graphDict[pair[1]].append((pair[0], 0))
            except KeyError:
                graphDict[pair[1]] = [(pair[0], 0)]
        line = fileObj.readline()
    return graphDict


def _parseNetworkEdges(fileObj):
    """
    Parses the network edges in task 2 graphs format file.
    :return: dict containing all the edges their capacities in KVP format 'v1' : [('v2', capacity), ...]
    """
    graphDict = {}

    for line in fileObj:
        (vertices, edgeCost) = re.findall(NETWORK_EDGE_PATTERN, line)
        vertices = re.findall(NUM_PATTERN, vertices)

        try:
            graphDict[vertices[0]].append((vertices[1], int(edgeCost)))
        except KeyError:
            graphDict[vertices[0]] = [(vertices[1], int(edgeCost))]

        try:
            graphDict[vertices[1]].append((vertices[0], int(edgeCost)))
        except KeyError:
            graphDict[vertices[1]] = [(vertices[0], int(edgeCost))]
    return graphDict


def _parseList(line):
    """
    Parses the eStart and seq lists in task 1 graphs format file.
    :return: list containing all the 1 character strings specified in input file.
    """
    return re.findall(LIST_ENTRIES_PATTERN, line)


def _usage(msg=""):
    """
    Usage method explaining to user how to use this script.
    :param msg: optional message to give to user
    """
    print "%susage: parser file_name -[task number]" % msg
    sys.exit(1)


def task1parse(fileObj):
    nEdges = _parseNumber(fileObj.readline())
    nNodes = _parseNumber(fileObj.readline())
    graphDict = _parseENodes(fileObj)
    eStart = _parseList(fileObj.readline())
    seq = _parseList(fileObj.readline())

    return (nEdges, nNodes, graphDict, eStart, seq)


def task2parse(fileObj):
    nEdges = _parseNumber(fileObj.readline())
    nNodes = _parseNumber(fileObj.readline())
    graphDict = _parseNetworkEdges(fileObj)

    return (nEdges, nNodes, graphDict)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        _usage()

    try:
        fileObj = open(sys.argv[1])

        # Task 1 arg
        if sys.argv[2] == '-1':
            t1 = task1parse(fileObj)
            print "nEdges: %d\nnNodes: %d\ngraphDict: %s\neStart: %s\nseq: %s\n" % t1
        # Task 2 arg
        elif sys.argv[2] == '-2':
            t2 = task2parse(fileObj)
            print "nEdges: %d\nnNodes: %d\ngraphDict: %s\n" % t2
        # Invalid arg
        else:
            _usage()

    except IOError:
        _usage("%s ain't a file!\n" % sys.argv[1])
    finally:
        fileObj.close()



