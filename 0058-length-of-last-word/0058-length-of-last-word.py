class Solution(object):
    def lengthOfLastWord(self, s):
        right = len(s)-1

        while right>=0 and s[right]==' ':
            right -= 1

        length = 0    
        while right>=0 and s[right]!=' ':
            length+=1
            right -= 1
            
        return length     
        """
        :type s: str
        :rtype: int
        """
        