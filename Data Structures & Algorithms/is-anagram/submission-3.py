class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if the length of strings are the same
        if len(s) != len(t):
            return False
        # make the hasmaps
        countS, countT = {}, {}

        # count the occurence of each char in the strings and add them to the hashmap
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        # if the count of the chars are not the same in each string, return false
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True