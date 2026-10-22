class Solution:
    def isDivBy8(self, s):
        # code here
        return (int(s[-3:])%8 == 0)
