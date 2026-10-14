class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""
        
        nines = sum // 9
        remainder = sum % 9
        zeros = num - nines - (1 if remainder > 0 else 0)
        
        # Build the lexicographically largest string
        res = "9" * nines
        if remainder > 0:
            res += str(remainder)
        res += "0" * zeros
        
        return res