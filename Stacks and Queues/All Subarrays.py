from collections import deque
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        lena=len(A)
        sf,sb=deque(),deque()
        i=0
        ans=-1
        while(i<lena):
            while(sf and A[sf[-1]]<=A[i]):
                ans=max(A[i]^A[sf[-1]],ans)
                sf.pop()
            sf.append(i)
    
            while(sb and A[sb[-1]]<=A[lena-i-1]):
                ans=max(A[lena-i-1]^A[sb[-1]],ans)
                sb.pop()
            sb.append(lena-i-1)
            i+=1
        
        return ans