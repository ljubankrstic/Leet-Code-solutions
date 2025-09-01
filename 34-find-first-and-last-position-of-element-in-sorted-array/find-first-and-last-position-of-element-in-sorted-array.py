class Solution(object):
    def searchRange(self, nums, target):
        if nums == []:
            return [-1,-1]
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] > target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
            else:
                start = middle
                break
        if start < 0 or start >= len(nums) or nums[start]!=target:
            return [-1,-1]
        end = start
        while end < len(nums) and nums[end] == target:
            end += 1
        end -= 1
        while nums[start] == target and start >=0:
            start -= 1
        start += 1
        return [start,end]
