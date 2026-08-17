class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        else:
            for i in range(len(nums)):
                if target<nums[i]:
                    return i
            else:
                return i+1