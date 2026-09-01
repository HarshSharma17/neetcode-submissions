class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            numset.add(nums[i])

        longestsub = 1

        for num in numset:
            if num - 1 in numset:
                continue
            else:
                currentnum = num
                commonsub = 1
                while currentnum + 1 in numset:
                    currentnum +=1
                    commonsub +=1
                
            longestsub = max(commonsub,longestsub)

        return longestsub