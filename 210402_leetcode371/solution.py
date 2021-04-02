class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        int_max = 0x7fffffff
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            
        if a > int_max:
            a = ~(a ^ mask)
            
        return a