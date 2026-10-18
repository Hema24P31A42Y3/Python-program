class Solution:
    def sumOfSeries(self,n):
        #code here
        
        total = 0
        for i in range(1,n+1):
            total = total + i**3
        return total
     
