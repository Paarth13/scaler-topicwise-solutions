def DFS(adj_lis,vis,se,element):
    vis[element]=1
    val=1
    se.add(element)
    for i in adj_lis[element]:
        if i in se:
            return 0
        if vis[i]!=1:
            val=DFS(adj_lis,vis,se,i)
            if val==0:
                return 0
    se.remove(element)
    return 1
class Solution:
	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):
	    vis=[0]*(A+1)
	    lenb=len(B)
	    se={-1}
	    adj_lis=[[] for i in range(A+1)]
	    for i in range(lenb):
	        adj_lis[B[i]].append(C[i])
	    for i in range(1,A+1):
	        if vis[i]==0:
	            vis[i]=1
	            if DFS(adj_lis,vis,se,i)==0:
	                return 0
	    return 1