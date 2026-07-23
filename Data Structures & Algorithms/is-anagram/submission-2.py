from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)
        for string in s:
            freq_s[string] += 1
        for strin in t:
            freq_t[strin] += 1

        if freq_s == freq_t:
            return True
        else:
            return False