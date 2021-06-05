import sys
sys.setrecursionlimit(10**6)

DIR = [[0,1],[1,0],[-1,0],[0,-1],[1,-1],[-1,1],[1,1],[-1,-1]]

tc = 0

visited = [[0 for j in range(105)]for i in range(105)]

def check(i, j, n, m,A):
    global visited,tc
    return (i>=0 and i<n and j>=0 and j<m and (A[i][j]==1) and visited[i][j]!=tc)

def dfs( i, j, n, m, A):
    global visited,tc
    visited[i][j] = tc
    for k in range(8):
        di = i+DIR[k][0]
        dj = j+DIR[k][1]
        if(check(di,dj,n,m,A)):
            dfs(di,dj,n,m,A)


def solveit(A):
    global visited,tc
    n = len(A)
    m = len(A[0])
    tc += 1
    numberofislands=0
    for i in range(n):
        for j in range(m):
            if(A[i][j]==1 and visited[i][j]!=tc):
                    dfs(i,j,n,m,A)
                    numberofislands+=1
                
    return numberofislands


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        return solveit(A)