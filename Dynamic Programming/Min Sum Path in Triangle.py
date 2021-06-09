class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        row=len(A)
        if row==1:
            return A[0][0]
        if row ==2:
            return A[0][0]+min(A[1][0],A[1][1])
        col=len(A[row-2])
        for i in range(row-2,-1,-1):
            for j in range(col):
                A[i][j]+=min(A[i+1][j],A[i+1][j+1])
            col-=1
        return A[0][0]
