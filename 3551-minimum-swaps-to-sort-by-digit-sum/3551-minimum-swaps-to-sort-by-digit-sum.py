class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        n = len(nums)
        # Pair each number with its (digit_sum, original_value, original_index)
        indexed_nums = []
        for i, val in enumerate(nums):
            indexed_nums.append((get_digit_sum(val), val, i))
            
        # Sort based on digit sum, then by value
        sorted_indexed = sorted(indexed_nums, key=lambda x: (x[0], x[1]))
        
        # Find minimum swaps using cycle decomposition
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or sorted_indexed[i][2] == i:
                continue
                
            # Traverse the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = sorted_indexed[curr][2]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps        