class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}":"{","]":"[",")":"("}
        stack = []

        for i in s:
            if stack and i in pairs and stack[-1] == pairs[i]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0

