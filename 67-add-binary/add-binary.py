class Solution(object):
    def addBinary(self, a, b):
        length = max(len(a), len(b))
        padded_a = a.rjust(length, '0')
        padded_b = b.rjust(length, '0')
        print(padded_a)
        print(padded_b)
        resarr = []
        carry = '0'
        for i in range(length - 1, -1 , -1):
            if padded_a[i] == '1' and padded_b[i] == '1':
                if carry == '1':
                    resarr.append('1')
                    carry = '1'
                else:
                    resarr.append('0')
                    carry = '1'
            elif (padded_a[i] == '0' and padded_b[i] == '1') or (padded_a[i] == '1' and padded_b[i] == '0'):
                if carry == '1':
                    resarr.append('0')
                    carry = '1'
                else:
                    resarr.append('1')
                    carry = '0'
            else:
                if carry == '1':
                    resarr.append('1')
                    carry = '0'
                else:
                    resarr.append('0')
                    carry = '0'
        if carry == '1':
            resarr.append('1')
        return ''.join(resarr[::-1])
        