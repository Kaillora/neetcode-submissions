class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "]":"[", "}":"{"}
        stack = []

        for c in s:
            if stack and c in pairs and stack[-1] == pairs[c]:
                stack.pop()
            else:
                stack.append(c)
        return not stack