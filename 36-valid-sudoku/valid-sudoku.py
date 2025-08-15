class Solution(object):
    def isValidSudoku(self, board):
        return self.checkRows(board) and self.checkColumns(board) and self.checkBlocks(board)
    def checkRows(self, board):
        for i in board:
            nums = []
            for k in i:
                if k != '.':
                    if k in nums:
                        return False
                    else:
                        nums.append(k)
        return True
    def checkColumns(self, board):
        for i in range(9):
            nums = []
            for k in board:
                if k[i] != '.':
                    if k[i] in nums:
                        return False
                    else:
                        nums.append(k[i])
        return True

    def checkBlocks(self, board):
        for row in [0, 1, 2]:
            for column in [0, 1, 2]:
                num_arr = []
                for x in [0, 1, 2]:
                    for y in [0, 1, 2]:
                        item = board[row * 3 + y][column * 3 + x]
                        if item != '.':
                            if item in num_arr:
                                return False
                            else:
                                num_arr.append(item)
        return True