from GraphAdjacencyList import Graph


class BFS:
    def __init__(self, adj_list):
        self.queue = []
        self.visited = [0]*(len(adj_list))
        self.adj_list = adj_list

    def bfs(self, source):
        # adding the source to queue and mark it visited
        self.queue.append(source)
        self.visited[source] = 1

        while self.queue:
            vertex = self.queue.pop(0)
            for connected_vertex in self.adj_list[vertex]:
                if self.visited[connected_vertex] == 0:
                    self.queue.append(connected_vertex)
                    # this prevents redundant addition of elements that are already in queue but not popped
                    self.visited[connected_vertex] = 1

            print(vertex)


graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
bfs = BFS(graph.get_graph())
bfs.bfs(2)
