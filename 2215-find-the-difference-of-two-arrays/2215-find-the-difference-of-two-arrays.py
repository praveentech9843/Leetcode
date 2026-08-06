class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[]
        ch1=[]
        ch2=[]
        for i in nums1:
            if i not in nums2 and i not in ch1:
                ch1.append(i)
        for i in nums2:
            if i not in nums1 and i not in ch2:
                ch2.append(i)
        ans.append(ch1)
        ans.append(ch2)
        return ans