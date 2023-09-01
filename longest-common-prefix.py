class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        f = strs[0]
        s = strs[1:]
        j = 0
        res = ""
        while True:
            try:
                c = 0
                for i in s:
                    if f[j] == i[j]:
                        c += 1
                if c == len(s):
                    res += f[j]
                else:
                    break
                j += 1
            except:
                break
        if res:
            return res
        else:
            return ""
