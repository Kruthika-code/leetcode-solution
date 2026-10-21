class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # Case 0: Already sorted
        if s == "".join(sorted(s)):
            return 0
            
        # If length is 2 and not sorted, it's impossible
        if n == 2:
            return -1
            
        min_char = min(s)
        max_char = max(s)
        
        # Case 1: Minimum character is at the start (proper prefix) 
        # or maximum character is at the end (proper suffix)
        if s[0] == min_char or s[-1] == max_char:
            return 1
            
        # Check if it's possible to sort at all (e.g., descending strings of length > 2 like "edc")
        # If the string consists of unique max at the start and unique min at the end
        if s.count(max_char) == 1 and s[0] == max_char and s.count(min_char) == 1 and s[-1] == min_char:
            return 3
            
        return 2