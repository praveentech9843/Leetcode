class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left=0
        count={}
        ans=0
        for right in range(len(nums)):
            num=nums[right]
            if num in count:
                count[num]+=1
            else:
                count[num]=1
            while count[num]>k:
                count[nums[left]]-=1
                left+=1
            leng=right-left+1
            if leng>ans:
                ans=leng
        return ans