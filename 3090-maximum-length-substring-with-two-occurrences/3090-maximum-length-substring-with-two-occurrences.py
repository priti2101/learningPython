class Solution(object):
    def maximumLengthSubstring(self, s):
        left = 0
        max_len = 0
        counts={}

        for right in range(len(s)):
            char = s[right]
            
            counts[char] = counts.get(char, 0) + 1

            # 2. Shrink window if count exceeds 2 📐
            while counts[char] > 2:
                counts[s[left]] -= 1
                left += 1

            # 3. Update maximum length found so far 📏
            max_len = max(max_len, right - left + 1)

        return max_len
        """
        :type s: str
        :rtype: int
        """
        