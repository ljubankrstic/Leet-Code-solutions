import numpy as np
class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j<=i:
                    continue
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        row_length = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j>=int(row_length/2):
                    continue
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][row_length - 1 - j]
                matrix[i][row_length - 1 - j] = temp
        return matrix