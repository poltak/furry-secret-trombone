import sys
import re

# Regex patterns to match valid input files
NUM_PATTERN = r"\d+"
E_NODES_PATTERN = r"\d+, \d+"
NETWORK_EDGE_PATTERN = r"(\d+ \d+|\d+)"
LIST_ENTRIES_PATTERN = r"(G|T|C|A)"


def _parse_number(line):
    """
    Parses all lines in task 1 and 2 graphs format files that contain single numbers.
    :return: int containing value found on specific line in input file.
    """
    match = re.findall(NUM_PATTERN, line)
    return int(match[0])


def _parse_e_nodes(file_obj):
    """
    Parses the e_nodes list in task 1 graphs format file.
    :return: dict containing all the edges their capacities in KVP format 'v1' : [('v2', capacity), ...]
    """
    graph_dict = {}

    line = file_obj.readline()
    while line != "];\n":
        pairs = []
        found = re.findall(E_NODES_PATTERN, line)
        for pair in found:
            pairs.append([digit for digit in re.findall(NUM_PATTERN, pair)])

        for pair in pairs:
            try:
                graph_dict[pair[0]].append((pair[1], 0))
            except KeyError:
                graph_dict[pair[0]] = [(pair[1], 0)]

            try:
                graph_dict[pair[1]].append((pair[0], 0))
            except KeyError:
                graph_dict[pair[1]] = [(pair[0], 0)]
        line = file_obj.readline()
    return graph_dict


def _parse_network_edges(file_obj):
    """
    Parses the network edges in task 2 graphs format file.
    :return: dict containing all the edges their capacities in KVP format 'v1' : [('v2', capacity), ...]
    """
    graph_dict = {}

    for line in file_obj:
        (vertices, edge_cost) = re.findall(NETWORK_EDGE_PATTERN, line)
        vertices = re.findall(NUM_PATTERN, vertices)

        try:
            graph_dict[vertices[0]].append((vertices[1], int(edge_cost)))
        except KeyError:
            graph_dict[vertices[0]] = [(vertices[1], int(edge_cost))]

        try:
            graph_dict[vertices[1]].append((vertices[0], int(edge_cost)))
        except KeyError:
            graph_dict[vertices[1]] = [(vertices[0], int(edge_cost))]
    return graph_dict


def _parse_list(line):
    """
    Parses the e_start and seq lists in task 1 graphs format file.
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


def task1parse(file_obj):
    n_edges = _parse_number(file_obj.readline())
    n_nodes = _parse_number(file_obj.readline())
    graph_dict = _parse_e_nodes(file_obj)
    e_start = _parse_list(file_obj.readline())
    seq = _parse_list(file_obj.readline())

    return (n_edges, n_nodes, graph_dict, e_start, seq)


def task2parse(file_obj):
    n_edges = _parse_number(file_obj.readline())
    n_nodes = _parse_number(file_obj.readline())
    graph_dict = _parse_network_edges(file_obj)

    return (n_edges, n_nodes, graph_dict)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        _usage()

    try:
        file_obj = open(sys.argv[1])

        # Task 1 arg
        if sys.argv[2] == '-1':
            t1 = task1parse(file_obj)
            print "n_edges: %d\nn_nodes: %d\ngraph_dict: %s\ne_start: %s\nseq: %s\n" % t1
        # Task 2 arg
        elif sys.argv[2] == '-2':
            t2 = task2parse(file_obj)
            print "n_edges: %d\nn_nodes: %d\ngraph_dict: %s\n" % t2
        # Invalid arg
        else:
            _usage()

    except IOError:
        _usage("%s ain't a file!\n" % sys.argv[1])
    finally:
        file_obj.close()



