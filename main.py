from parser import createSectOneGraph
import graphUtils
import sys

if __name__ == "__main__":
  g, seq = createSectOneGraph(sys.argv[1])
  for circuit in graphUtils.getEulerianCircuits(g):
    labels = graphUtils.getLabelsForPath(g, circuit)
    print graphUtils.long_substr([seq, labels])

    both = [seq, labels]



