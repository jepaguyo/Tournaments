class Matrix:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.adj = self.adjacency_matrix()

    def zero_matrix(self):
        m = []
        for i in range(self.n):
            m.append([0]*self.n)
        return m

    def adjacency_matrix(self):
        m = self.zero_matrix()
        for (i,j) in self.edges:
            m[i-1][j-1] = 1
        return m
