class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        result = -float('inf')
        min_so_far = nums[0]
        for i in range(1,len(nums)):
            result = max(nums[i] - min_so_far,result)
            min_so_far = min(min_so_far,nums[i])
        if result<=0:
            return -1
        else:
            return result
