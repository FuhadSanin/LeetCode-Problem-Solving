class Solution:
    def addBinary(self, a: str, b: str) -> str:
        an = 0
        for i, n in enumerate(a[::-1]):
            if n == "1":
                an += 2**i
        bn = 0
        for i, n in enumerate(b[::-1]):
            if n == "1":
                bn += 2**i
        sum = an + bn
        return bin(sum)[2:]
