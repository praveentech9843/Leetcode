class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ch=[]
        a=0
        ch.append(a)
        for i in range(len(gain)):
            a+=gain[i]
            ch.append(a)
        return max(ch)
