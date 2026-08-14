class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count={}
        ans=0
        left=0
        for right in range(len(s)):
            ch=s[right]
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
            while count[ch]>2:
                count[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans