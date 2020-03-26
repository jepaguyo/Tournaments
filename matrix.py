class Matrix:
    def __init__(self, n, edges):
        self.adj = self.adjacency_matrix(n, edges)

    def zero_matrix(self, n):
        m = []
        for i in range(n):
            m.append([0]*n)
        return m

    def adjacency_matrix(self, n, edges):
        m = self.zero_matrix(n)
        for (i,j) in edges:
            m[i-1][j-1] = 1
        return m

print(Matrix(3,[(1,1),(1,2),(3,1)]))
