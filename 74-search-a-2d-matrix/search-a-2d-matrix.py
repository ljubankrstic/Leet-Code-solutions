class Solution(object):
    def searchMatrix(self, matrix, target):
        start = 0
        end = len(matrix) - 1
        while start <= end:
            middle = (start + end) // 2
            if target > matrix[middle][0]:
                start = middle + 1
            if target < matrix[middle][0]:
                end = middle - 1
            if target == matrix[middle][0]:
                return True
        if start == 0:
            return False
        print(matrix[start - 1])
        target_arr = start - 1
        start, end = 0, len(matrix[target_arr]) - 1
        while start <= end:
            middle = (start + end) // 2
            if target == matrix[target_arr][middle]:
                return True
            elif target < matrix[target_arr][middle]:
                end = middle - 1
            else:
                start = middle + 1
        return False
        