from collections import deque
inf = 99999999
DIR = [[0,1],[1,0],[0,-1],[-1,0]]

def solveit(A):
    n = len(A)
    m = len(A[0])
    q = deque()
    distance = [[inf for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if(A[i][j]==1):
                distance[i][j]=0
                q.append([i,j])
            
    while(len(q) != 0):
        xy = q.popleft()
        x = xy[0]
        y = xy[1]
        
        for k in range(4):
            dx=x+DIR[k][0]
            dy=y+DIR[k][1]
            if(dx >=0 and dx<n and dy>=0 and dy<m and distance[dx][dy]>distance[x][y]+1):
                distance[dx][dy]=distance[x][y]+1
                q.append([dx,dy])
            
    return distance


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        return solveit(A)
