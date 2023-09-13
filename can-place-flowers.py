class Solution:
    def canPlaceFlowers(self, a: List[int], n: int) -> bool:
        c = 0
        if len(a) == 1 and 0 in a and n == 1:
            return True
        for i in range(len(a)):
            try:
                if a[i] == 0:
                    if (i == 0 and a[i+1] == 0) or (i == len(a)-1 and a[i-1] == 0) or (a[i-1] == 0 and a[i+1] == 0):
                        a[i] = 1
                        c += 1
            except:
                pass
        return True if c >= n else False
