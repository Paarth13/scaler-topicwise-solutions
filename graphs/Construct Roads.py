mod=10**9+7
from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def BFS(self,adj_lis,vis,A):
        q=deque()
        cou=0
        for j in range(A+1):
            if vis[j]!=-1 or not adj_lis[j]:
                continue
            vis[j]=1
            q.append(j)
            while q:
                val_pop=q.popleft()
                # print(val_pop,j)
                for i in range(len(adj_lis[val_pop])):
                    if vis[adj_lis[val_pop][i]]==-1:
                        vis[adj_lis[val_pop][i]]=vis[val_pop]^1
                        q.append(i)
                    elif vis[adj_lis[val_pop][i]]==vis[val_pop]:
                        vis[val_pop]^=1
        val=vis.count(0)
        A-=val
        return A*val 
                
        
    def solve(self, A, B):
        vis=[-1]*(A+1)
        adj_lis=[[] for i in range(A+1)]
        for i in B:
            adj_lis[i[0]].append(i[1])
        num=self.BFS(adj_lis,vis,A)
        return (num-A+1)%mod