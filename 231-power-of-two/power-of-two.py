class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        bn = bin(n)[2:]
        if bn.count('1')>1:
            return False
        return True
        