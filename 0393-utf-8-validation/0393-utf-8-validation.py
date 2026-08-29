class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        r=0
        for num in data:
            if r==0:
                if num>>7==0:
                    r=0
                elif num>>5==0b110:
                    r=1
                elif num>>4==0b1110:
                    r=2
                elif num>>3==0b11110:
                    r=3
                else:
                    return False
            else:
                if num>>6!=0b10:
                    return False
                r-=1
        return r==0