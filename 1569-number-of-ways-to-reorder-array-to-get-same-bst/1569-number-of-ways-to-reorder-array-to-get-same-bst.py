class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def helper(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            left_ways = helper(left)
            right_ways = helper(right)
            
            # Combinatorics: choose len(left) positions out of len(left) + len(right)
            comb = math.comb(len(left) + len(right), len(left))
            
            return (left_ways * right_ways * comb) % MOD
            
        # Subtract 1 because the original array ordering itself shouldn't be counted as a "reordering"
        return (helper(nums) - 1 + MOD) % MOD