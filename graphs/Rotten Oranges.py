from collections import deque
DIR = [[0,1],[1,0],[0,-1],[-1,0]]
class Solution:
    # @param A : list of list of integers
    # @return an integer
    
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        q = deque()
        t,cou1=0,0
        for i in range(n):
            for j in range(m):
                if(A[i][j]==2):
                    # distance[i][j]=2
                    q.append([i,j,t])
                if A[i][j]==1:
                    cou1+=1
        tnew=0
        while(len(q) != 0):
            xy = q.popleft()
            tnew=xy[2]+1
            x = xy[0]
            y = xy[1]
            
            for k in range(4):
                dx=x+DIR[k][0]
                dy=y+DIR[k][1]
                if(dx >=0 and dx<n and dy>=0 and dy<m and A[dx][dy]==1):
                        A[dx][dy]+=1
                        q.append([dx,dy,tnew])
                        cou1-=1
        return tnew-1 if cou1==0 else -1
        