class Solution:
    def factorial(self, n: int) -> int:
        # code here
        count = 1
        for i in range(1,n+1):
            count *= i
        return count
