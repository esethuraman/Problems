from __future__ import print_function
from DirectedGraph import DirectedGraph


class TransposeGraph:

    def __init__(self):
        self.graph = []
        self.visited = []
        pass

    def transpose_util(self, v, transpose):
        self.visited[v] = True
        if self.graph[v] is not None:
            for adj_vertex in self.graph[v]:
                if not transpose[adj_vertex]:
                    transpose[adj_vertex] = []
                transpose[adj_vertex].append(v)

    def transpose(self, graph):
        self.graph = graph
        self.visited = [False] * len(graph)
        transpose_graph = [None] * len(graph)
         
        for vertex in range(len(graph)):
            if not self.visited[vertex]:
                self.transpose_util(vertex, transpose_graph)
        return transpose_graph

    @staticmethod
    def display_graph(graph):
        for v in range(len(graph)):
            print(v, " --> ", end=" ")
            if graph[v] is not None:
                for adj_v in graph[v]:
                    print(adj_v, end=" ")
            print()


g = DirectedGraph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
TransposeGraph().display_graph(g.get_graph())
print("Transposed ---> ")
obj = TransposeGraph()
trans = obj.transpose(g.get_graph())
obj.display_graph(trans)


