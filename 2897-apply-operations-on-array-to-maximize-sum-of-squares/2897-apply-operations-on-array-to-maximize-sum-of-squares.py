class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31
        
        # Count set bits at each position
        for x in nums:
            for b in range(31):
                if (x >> b) & 1:
                    bit_counts[b] += 1
                    
        # Reconstruct the top k numbers to maximize sum of squares
        final_nums = [0] * k
        for b in range(31):
            count = bit_counts[b]
            for i in range(min(count, k)):
                final_nums[i] |= (1 << b)
                
        # Calculate the sum of squares modulo 10^9 + 7
        ans = 0
        for x in final_nums:
            ans = (ans + x * x) % MOD
            
        return ans