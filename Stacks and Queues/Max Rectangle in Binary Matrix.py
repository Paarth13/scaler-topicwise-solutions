from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def largestRectangleArea(self, A):
	    if len(A)==1:
	        return A[0]
	    rightBound,leftBound=[len(A)]*len(A),[-1]*len(A)
	    s=deque()
	    for i in range(len(A)):
	        if s:
	            while(s and A[s[-1]]>=A[i]):
	                s.pop()
	            if s:
	                leftBound[i]=s[-1]
	            else:
	                leftBound[i]=-1
	            s.append(i)
	        else:
	            s.append(i)
	    s=deque()
	    for i in range(len(A)-1,-1,-1):
	        if s:
	            while(s and A[s[-1]]>=A[i]):
	                s.pop()
	            if s:
	                rightBound[i]=s[-1]
	            else:
	                rightBound[i]=len(A)
	            s.append(i)
	        else:
	            s.append(i)
	   # print(leftBound,rightBound)
	    ans=0
	    for i in range(len(A)):
	        x=i-(leftBound[i])
	        x+=rightBound[i]-i-1
	        if x==0:
	            x=A[i]
	        else:
	            x*=A[i]
	       # print(x,rightBound[i],leftBound[i])
	        ans=max(x,ans)
	   # print(ans)
	    return ans
    def maximalRectangle(self, A):
        ans=0
        B=A.copy()
        for i in range(1,len(A)):
            for j in range(len(A[0])):
                if B[i][j]==1:
                    B[i][j]+=B[i-1][j]
        for i in B:
            ans=max(ans,self.largestRectangleArea(i))
        return ans