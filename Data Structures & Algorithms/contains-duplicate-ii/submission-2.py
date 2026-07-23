class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}  # number -> last index
        
        for i in range(len(nums)):
            if nums[i] in seen:
                # check distance
                if i - seen[nums[i]] <= k:
                    return True
            
            # update last seen index
            seen[nums[i]] = i
        
        return False