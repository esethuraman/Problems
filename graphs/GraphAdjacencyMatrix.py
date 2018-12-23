class Graph:

    def __init__(self, vertices_count):
        self.adj_mtrx = [[-1] * vertices_count for i in range(vertices_count)]
        self.vertices_count = vertices_count
        self.vertices_map = {}
        self.vertices_list = [0]*vertices_count

    def set_vertex(self, indx, id):
        if -1 < indx < self.vertices_count:
            self.vertices_map[id] = indx
            self.vertices_list[indx] = id

    def set_edge(self, frm, to, cost=0):
        frm = self.vertices_map[frm]
        to = self.vertices_map[to]
        self.adj_mtrx[frm][to] = cost
        self.adj_mtrx[to][frm] = cost

    def get_vertices(self):
        return self.vertices_list

    def get_edges(self):
        edges = []
        for i in range (self.vertices_count):
            for j in range (self.vertices_count):
                if self.adj_mtrx[i][j] != -1:
                    edg_tpl = (self.vertices_list[i], self.vertices_list[j], self.adj_mtrx[i][j])
                    edges.append(edg_tpl)
        return edges

    def get_matrix(self):
        return self.adj_mtrx

G = Graph(6)
G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
G.set_edge('a','e',10)
G.set_edge('a','c',20)
G.set_edge('c','b',30)
G.set_edge('b','e',40)
G.set_edge('e','d',50)
G.set_edge('f','e',60)
print("Vertices of Graph")
print(G.get_vertices())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())