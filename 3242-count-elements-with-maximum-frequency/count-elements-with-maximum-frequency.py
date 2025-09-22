class Solution(object):
    def maxFrequencyElements(self, nums):
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        maxfreq = 0
        for i in dic:
            if dic[i] > maxfreq:
                maxfreq = dic[i]
        res = 0
        for i in dic:
            if dic[i] == maxfreq:
                res += dic[i]
        return res
        