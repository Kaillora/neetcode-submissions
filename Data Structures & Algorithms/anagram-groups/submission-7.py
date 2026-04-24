class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26 # a...z
            for c in word:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(word)
        return list(anagrams.values())