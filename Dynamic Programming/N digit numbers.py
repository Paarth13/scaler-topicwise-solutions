mod=10**9+7
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def resp(self,dp,digits_left,sum_left):
	    if sum_left<0:
	        return 0
	    if digits_left==0 and sum_left==0:
	        return 1
	    if digits_left==0:
	        return 0
	    if dp[digits_left][sum_left]!=-1:
	        return dp[digits_left][sum_left]
	    ans=0
	    for i in range(10):
	        ans+=self.resp(dp,digits_left-1,sum_left-i)
	        ans%=mod
	    dp[digits_left][sum_left]=ans
	    return dp[digits_left][sum_left]
	    
	def solve(self, A, B):
	    dp=[[-1 for i in range(B+1)]for j in range(A+1)]
	    ans=0
	    
	    for i in range(1,10):
	        ans+=self.resp(dp,A-1,B-i)
	        ans%=mod
	    return ans