class DirectedGraph:

    def __init__(self, vertices_count):
        self.vertices_count = vertices_count
        self.adj_list = [None]*vertices_count

    def add_edge(self, frm, to):
        if self.adj_list[frm] is None:
            self.adj_list[frm] = []
        self.adj_list[frm].append(to)

    def get_graph(self):
        return self.adj_list
