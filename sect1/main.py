from parser import parseFile
import graphutils
import sys

def main(filePath):
    graph, sequence = parseFile(filePath)

    # Get all the possible Euler circuits in given graph.
    eulerCircuits = graphutils.getEulerianCircuits(graph)
    longestCommonSStrings = []
    circuitLabels = []

    # For each of the circuits found, get the circuit label string and also the longest common substring.
    for circuit in eulerCircuits:
        circuitLabel = graphutils.getLabelsForPath(graph, circuit)
        circuitLabels.append(circuitLabel)
        longestCommonSStrings.append(graphutils.longestCommonSubstring(sequence, circuitLabel))

    # Out of all the substrings, find the longest
    longestIndex = 0
    longestString = 0
    for i in range(len(longestCommonSStrings)):
        if len(longestCommonSStrings[i]) > longestString:
            longestString = len(longestCommonSStrings[i])
            longestIndex = i

    # The following is all for nice output
    print 'Eulerian Circuit: %s' % eulerCircuits[longestIndex]
    print 'Symbols on path: %s' % circuitLabels[longestIndex]
    print 'Sequence: %s' % sequence
    print 'Matched Substring: %s' % longestCommonSStrings[longestIndex]
    startIndexSeq = findStringIndex(sequence, longestCommonSStrings[longestIndex])
    startIndexCircuit = findStringIndex(circuitLabels[longestIndex], longestCommonSStrings[longestIndex])
    lengthSString = len(longestCommonSStrings[longestIndex]) -1
    print 'Found sequence: %d-%d and subsequence: %d-%d' % (startIndexSeq, startIndexSeq + lengthSString, startIndexCircuit, startIndexCircuit + lengthSString)

def findStringIndex(string, substring):
    """
    Simple utility method to make life easier for printing output.
    """
    index = 0

    c = substring[0]
    for ch in string:
        if ch == c:
            if string[index:index+len(substring)] == substring:
                return index
        index += 1

def usage():
    print 'usage: main.py [graph file]'
    sys.exit(1)

if __name__ == '__main__':
    # Basic arg checking
    if len(sys.argv) != 2: usage()

    main(sys.argv[1])
