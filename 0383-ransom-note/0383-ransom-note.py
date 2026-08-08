class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1={}
        for i in magazine:
            c1[i]=c1.get(i,0)+1
        for ch in ransomNote:
            if ch not in c1 or c1[ch]==0:
                return False
            c1[ch]-=1
        return True