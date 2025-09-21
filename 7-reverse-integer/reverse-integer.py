class Solution(object):
    def reverse(self, x):
        n = str(x)
        if x < 0:
            negative = True
            n = n[1:]
        else:
            negative = False
        n = n[::-1]
        n = int(n)
        if negative:
            n*=-1
        if n > 2**31-1 or n < -2**31:
            return 0
        return n
        