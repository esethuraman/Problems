from GraphAdjacencyList import Graph


class DisconnectedDFS:
    def __init__(self, adj_list):
        self.adj_list = adj_list
        self.vertices = [i for i in range(len(adj_list))]

    def dfs_helper(self, source, visited):
        visited[source] = 1
        print(source)
        for adj_vertex in self.adj_list[source]:
            if visited[adj_vertex] == 0:
                self.dfs_helper(adj_vertex, visited)

    def dfs(self):
        visited = [0]*len(self.vertices)
        for vertex in self.vertices:
            if visited[vertex] == 0:
                self.dfs_helper(vertex, visited)


graph = Graph(6)
# graph.add_edge(0, 1)
# graph.add_edge(0, 4)
graph.add_edge(0, 5)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
dfs = DisconnectedDFS(graph.get_graph())
print("DFS traversal of the given graph is :")
dfs.dfs()
