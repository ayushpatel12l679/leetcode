class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        i = 0
        j = len(s)-1
        isPalindrome = True
        while i<j:
            if s[i]!= s[j]:
                isPalindrome = False
                break
            else:
                i+=1
                j-=1
        return isPalindrome

      