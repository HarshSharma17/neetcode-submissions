from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashset = set(nums)
        longestSub = 0
        
        for num in hashset:
            # Only start counting if it's the beginning of a sequence
            if num - 1 not in hashset:
                currentNum = num
                currentSub = 1
                
                while currentNum + 1 in hashset:
                    currentNum += 1
                    currentSub += 1
                
                longestSub = max(longestSub, currentSub)
        
        return longestSub