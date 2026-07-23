class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        
        for i in range(len(nums)):
            # If window size exceeds k, remove the element
            # that is too far away
            if i > k:
                window.remove(nums[i - k - 1])
            
            # If number already exists in window → duplicate found
            if nums[i] in window:
                return True
            
            # Add current number to window
            window.add(nums[i])
        
        return False
