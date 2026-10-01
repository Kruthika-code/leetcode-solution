class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # 1. Ignore leading whitespace
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        # 2. Determine sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        num = 0
        # 3. Read valid digits
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
            
        num *= sign
        
        # 4. Clamp within 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
            
        return num

#Complexity
#Time Complexity:O(N), where N is the length of s, as we traverse the string at most once.
#Space Complexity:O(1) OR O(N) due to lstrip() string slicing, using constant auxiliary space.