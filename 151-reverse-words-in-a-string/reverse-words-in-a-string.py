class Solution(object):
    def reverseWords(self, s):
        mystr= s.strip()
        lst = mystr.split()
        lst = lst[::-1]
        sep = ' '
        return sep.join(lst)
        