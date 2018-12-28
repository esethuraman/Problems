from GraphAdjacencyList import Graph


class DFS:
    def __init__(self, adj_list):
        self.adj_list = adj_list

    def dfs_helper(self, source, visited):
        visited[source] = 1
        print(source)
        for adj_vertex in self.adj_list[source]:
            if visited[adj_vertex] == 0:
                self.dfs_helper(adj_vertex, visited)

    def dfs(self, source):
        visited = [0] * len(self.adj_list)
        visited[source] = 1
        self.dfs_helper(source, visited)


graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(0, 5)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
dfs = DFS(graph.get_graph())
dfs.dfs(1)
