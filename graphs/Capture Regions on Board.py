from collections import deque
inf = 99999999
DIR = [[0,1],[1,0],[0,-1],[-1,0]]
changed_indexes=[]
def DFS(i,j,vis,A,q,n,m):
    while(len(q) != 0):
        xy = q.popleft()
        x = xy[0]
        y = xy[1]
        vis[x][y]="X"
        changed_indexes.append((x,y))
        for k in range(4):
            dx=x+DIR[k][0]
            dy=y+DIR[k][1]
            if(dx >=0 and dx<n and dy>=0 and dy<m and vis[dx][dy]=="O"):
                q.append([dx,dy])

def solveit(A):
    n = len(A)
    m = len(A[0])
    q = deque()
    for i in range(n):
        A[i]=list(A[i])
    vis=A.copy()
    # print(A)
    global changed_indexes
    changed_indexes=[]
    count=0
    for j in range(n):
            if (A[j][0]=="O" and vis[j][0]=="O"):
                q.append([j,0])
                DFS(j,0,vis,A,q,n,m)
            if (A[j][m-1]=="O" and vis[j][m-1]=="O"):
                q.append([j,m-1])
                DFS(j,m-1,vis,A,q,n,m)
    for j in range(m):
        if(A[0][j]=="O" and vis[0][j]=="O"):
                q.append([0,j])
                DFS(0,j,vis,A,q,n,m)
        
        if (A[n-1][j]=="O" and vis[n-1][j]=="O"):
            q.append([n-1,j])
            DFS(n-1,j,vis,A,q,n,m)
        
    # print(changed_indexes,vis)
    for i in range(n):
        for j in range(m):
            
            if vis[i][j]=="O":
                vis[i][j]="X"
    # print(vis)                  
    for i in changed_indexes:
        A[i[0]][i[1]]="O"
    # print(vis)
    for i in range(n):
        A[i]=''.join(A[i])

    return vis


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        return solveit(A)
