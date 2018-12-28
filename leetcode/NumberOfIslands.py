
class NumberOfIslands:
    def num_islands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        adj_list = self.construct_adj_lst_frm_matrix(grid)
        print(adj_list)
        print(self.dfs(adj_list))

    def construct_adj_lst_frm_matrix(self, grid):
        adj_lst = [None]*len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if adj_lst[i] is None:
                        adj_lst[i] = []
                    adj_lst[i].append(j)
        return adj_lst

    def dfs(self, adj_list):
        count = 0
        vertices = [i for i in range(len(adj_list))]
        visited = [False] * len(vertices)
        for v in vertices:
            if not visited[v]:
                self.dfs_util(adj_list, v, visited)
                count += 1
        print("Number of islands : ", count)

    def dfs_util(self, graph, v, visited):
        visited[v] = True
        print(v)
        if graph[v] is not None and v < len(graph):
            for adj_v in graph[v]:
                if not visited[adj_v]:
                    visited[adj_v] = True
                    self.dfs_util(graph, adj_v, visited)


obj = NumberOfIslands()
g = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
# obj.num_islands(g)

g = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
obj.num_islands(g)
