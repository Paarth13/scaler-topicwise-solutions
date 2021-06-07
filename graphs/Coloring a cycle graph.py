class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A==1:
            return 1
        if A&1==0:
            return 2
        return 3