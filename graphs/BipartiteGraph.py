from DirectedGraph import DirectedGraph


class BipartiteGraph:

    def __init__(self):
        pass

    @staticmethod
    def is_bipartite(graph, src):
        color = [None] * len(graph)
        color[src] = "red"
        queue = [src]

        while queue:
            v = queue.pop(0)
            if graph[v]:
                for adj_v in graph[v]:
                    if color[adj_v] == color[v]:
                        return False
                    if color[adj_v] is None:
                        queue.append(adj_v)
                        color[adj_v] = "red" if color[v] == "black" else "black"

        return True


g = DirectedGraph(6)
g.add_edge(0, 2)
g.add_edge(2, 0)
g.add_edge(1, 2)
g.add_edge(0, 3)
g.add_edge(0, 4)
g.add_edge(0, 5)
g.add_edge(4, 5)
# g.add_edge(2, 3)
obj = BipartiteGraph()
# print(obj.is_bipartite(g.get_graph(), 0))

lst = [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]
print(obj.is_bipartite(lst, 2))


