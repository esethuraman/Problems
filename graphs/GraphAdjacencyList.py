class Graph:

    def __init__(self, vertices_count):
        self.vertices_count = vertices_count
        self.adj_list = [None] * vertices_count

    def add_edge(self, frm, to):
        if None == self.adj_list[frm]:
            self.adj_list[frm] = []
        if None == self.adj_list[to]:
            self.adj_list[to] = []
        self.adj_list[frm].append(to)
        self.adj_list[to].append(frm)

    def get_edges(self):
        for i in range(self.vertices_count):
            if self.adj_list[i] is not None:
                for j in range(len(self.adj_list[i])):
                    print(i, ' -> ', self.adj_list[i][j])

    def get_graph(self):
        return self.adj_list

    def build_graph(self):
        graph = Graph(6)
        graph.add_edge(0, 1)
        graph.add_edge(0, 4)
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)

        print("Edges of Graph")
        graph.get_edges()
        print("Adjacency List of Graph")
        print(graph.get_graph())


g = Graph(6)
g.build_graph()
