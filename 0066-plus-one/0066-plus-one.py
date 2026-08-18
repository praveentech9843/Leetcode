class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ""
        for i in digits:
            a += str(i)
        ans = int(a)+1
        s  = []
        for i in str(ans):
            s.append(int(i))
        return s    
           
        


