class Solution(object):
    def setZeroes(self, matrix):
        cols = []
        rows = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols.append(j)
                    rows.append(i)
        cols.sort()
        rows.sort()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0