class Solution:
    def reverseWords(self, s: str) -> str:
        ch=s.split()
        ans=""
        for i in range(len(ch)):
            a=ch[i]
            b=a[::-1]
            ans+=b
            if i!=len(ch)-1:
                ans+=" "
        return ans
