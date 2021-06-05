class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
	def DFS(self,adj_lis,source,destination,visited):
	    visited[source]=1
	    if source== destination:
	        return 1
	    for i in adj_lis[source]:
	        if visited[i]!=1:
	            c=self.DFS(adj_lis,i,destination,visited)
	            if c==1:
	                return 1
	    return 0
	    
	    
	def solve(self, A, B, C):
	    lena=len(A)
	    visited=[0]*(lena+1)
	    adj_lis=[[] for i in range(lena+1)]
	    for j in range(lena):
	        adj_lis[A[j]].append(j+1)
	   # print(adj_lis)
	    return self.DFS(adj_lis,C,B,visited)