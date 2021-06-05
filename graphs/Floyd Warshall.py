class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        lena=len(A)
        # print(A)
        inf=10**9
        for i in range(lena):
            for j in range(lena):
                if A[i][j]==-1:
                    A[i][j]=inf
        for k in range(lena):
            for i in range(lena):
                    for j in range(lena):
                        if A[i][j]>A[i][k]+A[k][j]:
                            A[i][j]=A[i][k]+A[k][j]
        for i in range(lena):
            for j in range(lena):
                if A[i][j]==inf:
                    A[i][j]=-1
        return A