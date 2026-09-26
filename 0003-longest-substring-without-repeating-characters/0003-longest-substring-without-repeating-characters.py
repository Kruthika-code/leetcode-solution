class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores character and its most recent index
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # If the character is already in the window, shrink the window from the left
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Update the latest position of the character
            char_map[char] = right
            
            # Calculate the current window length and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length