class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []
        for c in s:
            if c in d.values():
                stack.append(c)
            elif stack and stack[-1] == d.get(c):
                stack.pop()
            else:
                return False
        return True if not stack else False
