# Binary search logic
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        if num == 1:
            return True
        else:
            while l < r:
                mid = (l+r) // 2
                if mid * mid == num:
                    return True
                elif mid * mid > num:
                    r = mid
                else:
                    l = mid + 1
            return False
