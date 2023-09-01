class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res = []
        if n == 0:
            return []
        for i in range(1, n+1):
            j = 1
            ls, k = [], 0
            temp = res[-1] if res else 0
            while j <= i:
                if j == 1 or j == i:
                    ls.append(1)
                else:
                    ls.append(temp[k] + temp[k+1])
                    k += 1
                j += 1
            res.append(ls)
        return res
