class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
# Square all elements and sort them
        squares = sorted(x * x for x in nums)
        n = len(squares)
        
 # The first half (smaller elements) are subtracted, 
# the second half (larger elements) are added.
        mid = n // 2
        subtracted_sum = sum(squares[:mid])
        added_sum = sum(squares[mid:])
        
        return added_sum - subtracted_sum