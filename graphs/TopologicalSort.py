from DirectedGraph import DirectedGraph

"""
Intuition: Same as that of DFS, except for the fact while performing
            the traversal, push the visited vertices to stack instead 
            of printing. Finally pop the vertices from stack.
"""


class TopologicalSort:
    def __init__(self):
        pass

    def topological_sort(self, graph):
        visited = [False]*len(graph)
        stack = []
        # iterate through all the vertices to ensure disconnected vertices are included
        for vertex in range(len(graph)):
            # condition is important to not visit redundant vertices (i.e vertices
            # that are already in the recursion stack)
            if not visited[vertex]:
                self.topological_sort_util(graph, vertex, visited, stack)
        print("Topological sorted order of vertices: ", stack)

    def topological_sort_util(self, graph, source, visited, stack):
        visited[source] = True
        if graph[source]:
            for adj_vertex in graph[source]:
                if not visited[adj_vertex]:
                    self.topological_sort_util(graph, adj_vertex, visited, stack)
        stack.insert(0, source)


g = DirectedGraph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
TopologicalSort().topological_sort(g.adj_list)


