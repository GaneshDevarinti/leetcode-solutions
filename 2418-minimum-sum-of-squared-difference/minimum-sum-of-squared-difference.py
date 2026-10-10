class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        max_diff = max(diffs)

        if max_diff == 0:
            return 0

        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1
        k = k1 + k2

        for d in range(max_diff, 0, -1):
            if count[d] > 0:
                if k >= count[d]:
                    k -= count[d]
                    count[d - 1] += count[d]
                    count[d] = 0
                else:
                    count[d - 1] += k
                    count[d] -= k
                    k = 0
                    break 
                    
        return sum(d * d * count[d] for d in range(1, max_diff + 1))
