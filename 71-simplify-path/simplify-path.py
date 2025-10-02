class Solution(object):
    def simplifyPath(self, path):
        currword = ""
        arr = []
        i = 0
        while i < len(path):
            if path[i] == '/':
                if currword != "":
                    arr.append(currword)
                currword = ""
            else:
                currword += path[i]
            i += 1
        if currword != "":
            arr.append(currword)
        print(arr)
        mypath = ""
        stck = []
        for i in range(len(arr)):
            if arr[i] == '.':
                continue
            elif arr[i] == '..':
                if len(stck) > 0:
                    stck.pop()
            else:
                stck.append(arr[i])
        print(stck)
        for i in stck:
            mypath = mypath + '/' + i
        if mypath == "":
            mypath = "/"
        return mypath
        