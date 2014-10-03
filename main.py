from parser import task1parse, task2parse
from graph import Graph

if __name__ == "__main__":
    task1file = open("task1graphs/Fig1TEST")
    graph_dict = task1parse(task1file)

    graph = Graph(graph_dict[2])

    print graph

    task1file.close()
