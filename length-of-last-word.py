class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip()
        ls = s1.split(" ")
        return len(ls[len(ls)-1])
