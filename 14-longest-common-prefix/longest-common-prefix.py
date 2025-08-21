class Solution(object):
    def longestCommonPrefix(self, strs):
        t = strs[0]
        for i in strs:
            if len(i) < len(t):
                t = i
        while len(t) > 0:
            k = True
            for i in strs:
                if i[:len(t)] != t:
                    t = t[:-1]
                    k = False
                    break
            if k:
                return t
        return ""
        
        