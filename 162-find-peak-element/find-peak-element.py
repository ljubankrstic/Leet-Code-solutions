class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        for i in range(0, len(nums), 2):
            if i == 0:
                if nums[i + 1] < nums[i]:
                    return i
                continue
            if i == len(nums) - 1:
                if nums[i - 1] < nums[i]:
                    return i
                continue
            if nums[i + 1] < nums[i] and nums[i - 1] < nums[i]:
                return i
        for i in range(1, len(nums), 2):
            if i == len(nums) - 1:
                if nums[i - 1] < nums[i]:
                    return i
                continue
            if nums[i + 1] < nums[i] and nums[i - 1] < nums[i]:
                return i
        return -1 
        