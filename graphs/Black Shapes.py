from collections import deque
inf = 99999999
DIR = [[0,1],[1,0],[0,-1],[-1,0]]

def solveit(A):
    n = len(A)
    m = len(A[0])
    q = deque()
    vis=[list(i) for i in A]
    count=0
    for i in range(n):
        for j in range(m):
            if(A[i][j]=="X" and vis[i][j]=="X"):
                q.append([i,j])
                while(len(q) != 0):
                    xy = q.popleft()
                    x = xy[0]
                    y = xy[1]
                    vis[x][y]="O"
                    for k in range(4):
                        dx=x+DIR[k][0]
                        dy=y+DIR[k][1]
                        if(dx >=0 and dx<n and dy>=0 and dy<m and vis[dx][dy]=="X"):
                            q.append([dx,dy])
                count+=1
    return count


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def black(self, A):
        return solveit(A)
