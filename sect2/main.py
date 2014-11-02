import sys
from parser import createFlowGraph
from maxflow import maxFlow

def main(filePath):
    flowGraph, numVertices = createFlowGraph(filePath)

    # As per assignment specs, the source and sink will always be these vertices
    source = 0
    sink = numVertices-1

    # Calculate and print the max flow
    flow = maxFlow(flowGraph, source, sink)
    # print 'the calculated max flow is: %d' % flow
    print flow

def usage():
    print 'usage: main.py [graph file]'
    sys.exit(1)

if __name__ == '__main__':
    # Basic arg checking
    if len(sys.argv) != 2:  usage()

    main(sys.argv[1])
