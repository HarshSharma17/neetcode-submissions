class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        CharCount = [0] * 26

        for i in range(len(s)):
            CharCount[ord(s[i]) - ord('a')] += 1
            CharCount[ord(t[i]) - ord('a')] -= 1

        for num in CharCount:
            if num != 0:
                return False

        return True