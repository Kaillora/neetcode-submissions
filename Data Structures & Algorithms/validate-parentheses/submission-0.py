class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "]":"[", "}": "{"}

        for char in s:
            if stack and (char in pairs) and stack[-1] == pairs[char]:
                stack.pop()
            else:
                stack.append(char)
                
        return not stack