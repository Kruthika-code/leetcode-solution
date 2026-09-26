class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Iterate over characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Compare character with the same position in other strings
            for j in range(1, len(strs)):
                # If index is out of bounds or characters don't match
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
                    
        return strs[0]      