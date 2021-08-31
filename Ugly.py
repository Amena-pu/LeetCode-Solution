class Solution:
    def isUgly(self, n: int) -> bool:
        if(n>0):
            while(True):
                if(n%2==0):
                    n=n//2
                elif(n%3==0):
                    n=n//3
                elif(n%5==0):
                    n=n//5
                else:
                    if(n==1):
                        return True
                    else:
                        return False
        return False
           