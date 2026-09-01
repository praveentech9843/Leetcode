class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for x in nums1:
            i=nums2.index(x)
            found=-1
            for j in range(i+1,len(nums2)):
                if nums2[j]>x:
                    found=nums2[j]
                    break
            ans.append(found)
        return ans