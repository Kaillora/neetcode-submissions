class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countofS, countofT = {}, {}

        for i in range(len(s)):
            countofS[s[i]] = 1 + countofS.get(s[i], 0)
            countofT[t[i]] = 1 + countofT.get(t[i], 0)
        for c in countofS:
            if countofS[c] != countofT.get(c, 0):
                return False
        return True


