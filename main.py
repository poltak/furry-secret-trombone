from parser import createSectOneGraph
from graphUtils import getEdgeSet

if __name__ == "__main__":
  g = createSectOneGraph('testg1')
  t = getEdgeSet(g)
  print t