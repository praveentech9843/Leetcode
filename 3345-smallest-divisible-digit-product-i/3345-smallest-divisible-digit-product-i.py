class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        ans=n
        while True:
            ch=1
            for i in str(ans):
                ch*=int(i)
            if ch%t==0:
                return ans
                break
            else:
                ans+=1
    