class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ch=sum(nums)
        l=0
        for i in range(len(nums)):
            r=ch-l-nums[i]
            if l==r:
                return i
                break
            l+=nums[i]
        else:
            return -1