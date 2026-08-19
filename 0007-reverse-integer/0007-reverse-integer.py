class Solution:
    def reverse(self, x: int) -> int:
        s=1
        if x<0:
            s=-1
            x=-x
        ans=0
        while x>0:
            d=x%10
            ans=ans*10+d
            x=x//10
        ans=ans*s
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        return ans