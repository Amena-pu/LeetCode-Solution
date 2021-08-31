class Solution:
    def reverse(self, x: int) -> int:
        newno = 0
        no = abs(x)
        i = 0
        while no > 0:
            digit = 10 ** (i + 1)
            newno = (newno * digit) + no % 10
            no = no // 10
            
        if (newno > 2**31 -1) or (-newno < -2**31):
            return(0)
        if x >= 0:
            return newno
        else:
            return -newno