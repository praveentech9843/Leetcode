class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            ch=0
            for i in str(num):
                ch+=int(i)
            num=ch
        return num