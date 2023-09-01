class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        for i in range(len(s)-1):
            if roman.get(s[i]) < roman.get(s[i+1]):
                res -= roman.get(s[i])
            else:
                res += roman.get(s[i])
        res += roman.get(s[len(s)-1])
        return res