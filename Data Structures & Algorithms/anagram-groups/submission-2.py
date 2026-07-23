from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            freq = [0] * 26

            for char in word:
                freq[ord(char) - ord('a')] += 1

            key = tuple(freq)

            anagram_map[key].append(word)

        return list(anagram_map.values())