# Sliding window technique
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in x:
                x.remove(s[l])
                l += 1
            x.add(s[i])
            res = max(res, i - l + 1)
            print(x, res)
        return res
