class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        a=max(candies)
        for i in range(len(candies)):
            ch=candies[i]+extraCandies
            if a<=ch:
                ans.append(True)
            else:
                ans.append(False)
        return ans