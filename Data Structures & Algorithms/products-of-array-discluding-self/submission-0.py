class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        pre,post = 1,1

        for i in range(len(nums)):
            answer[i] = pre
            pre = nums[i] * pre

        for j in reversed(range(len(nums))):
            answer[j] *= post
            post = post * nums[j]

        return answer