import re

class Graph(dict):

    def __init__(self, graph_dict):
        """ Initializes a graph object """
        dict.__init__(self, "")
        self = graph_dict
        print self

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.keys())

    def are_adjacent(self, v1, v2):
        """
        :return: boolean denoting whether or not v1 and v2 are neighbours
        """
        return self[v1].contains(v2) and self[v2].contains(v1)

    def get_neighbours(self, v1):
        """
        :return: returns a list of neighbours from v1 (empty if none)
        """
        try:
            return self[v1]
        except KeyError:
            return []

    def add_edge(self, v1, v2):
        """
        Add edge from v1 to v2 if not already there.
        """
        return self[v1].add(v2) and self[v2].add(v1)

    def delete_edge(self, v1, v2):
        """
        Delete edge between v1 and v2 if it exists.
        """
        return self[v1].remove(v2) and self[v2].remove(v1)

    def get_edge_capacity(self, v1, v2):
        if not are_adjacent(v1, v2):
            return False
        return self[v1][indexOfV2][1]

    def set_edge_capacity(self, v1, v2, new_value):
        if not are_adjacent(v1, v2):
            return False
        pass




    def __generate_edges(self):
        edges = []
        for vertex in self:
            for neighbour in self[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        tostring = ""
        # TODO: look at iterating over dicts
        for vertex in self.keys():
            neighbour_str = ""
            for neighbour in self[vertex]:
                neighbour_str += "\tvertex %s (capacity: %s)\n" % (neighbour[0] , neighbour[1])

            tostring += "vertex %s :\nneighbouring vertices:\n%s\n" % (vertex, neighbour_str)

        return tostring

