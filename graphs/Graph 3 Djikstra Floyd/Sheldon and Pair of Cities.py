class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @param G : list of integers
    # @param H : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F, G, H):
        inf = 10**9
        lena = A+1
        adj_arr = [[inf for i in range(A+1)]for j in range(A+1)]
        for i in range(A+1):
            adj_arr[i][i] = 0
           # Key Observation
        for i in range(B):
            adj_arr[D[i]][E[i]] = min(adj_arr[D[i]][E[i]], F[i])
            adj_arr[E[i]][D[i]] = min(adj_arr[E[i]][D[i]], F[i])
        for k in range(lena):
            for i in range(lena):
                for j in range(lena):
                    if adj_arr[i][j] > adj_arr[i][k]+adj_arr[k][j]:
                        adj_arr[i][j] = adj_arr[i][k]+adj_arr[k][j]

        ans = []
        for i in range(C):
            if adj_arr[G[i]][H[i]] == inf:
                ans.append(-1)
            else:
                ans.append(adj_arr[G[i]][H[i]])
        return ans
