class Solution(object):
    def reverseString(self, s):
        j = 0
        i = len(s)-1
        while i>j:
            s[i],s[j] = s[j],s[i]
            i-=1
            j+=1
        