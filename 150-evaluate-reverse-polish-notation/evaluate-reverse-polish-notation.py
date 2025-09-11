class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = '+-*/'
        nums = []
        for i in tokens:
            if i not in op:
                nums.append(int(i))
            else:
                op2 = nums.pop()
                op1 = nums.pop()
                if i == '+':
                    nums.append(op1 + op2)
                elif i == '-':
                    nums.append(op1 - op2)
                elif i == '*':
                    nums.append(op1 * op2)
                else:
                    nums.append(int(op1/op2))
        return nums[0]
        