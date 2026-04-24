from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # turn the list into a dictionary for hashing
        anagrams = defaultdict(list)
        # for each string, make an array for every letter in the alphabet to count
        # the frequency of the letters. turn the letter count into a tuple, check
        # if in list, then add the string to the anagram list if needed
        for s in strs:
            count  = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        # return just the values, not the index, of the anagram list.
        return list(anagrams.values())
