import sys
sys.setrecursionlimit(10**9)
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def DFS(self,adj_lis,vis,node,parent):
        vis[node]=1
        parent.add(node)
        for i in adj_lis[node]:
            # print(i,parent)
            if vis[i]!=1:
                if self.DFS(adj_lis,vis,i,parent)==1:
                    return 1
            elif (i in parent):
                return 1
        parent.remove(node)
        return 0
    def solve(self, A, B):
        vis=[0]*(A+1)
        parent={0}
        adj_lis=[[] for i in range(A+1)]
        for i in B:
            adj_lis[i[0]].append(i[1])
        # print(adj_lis)
        for i in range(1,A+1):
            if vis[i]==0 and self.DFS(adj_lis,vis,i,parent):
                return 1
        return 0