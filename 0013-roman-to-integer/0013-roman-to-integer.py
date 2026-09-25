class Solution:
    def romanToInt(self, s: str) -> int:
        # Map of Roman numerals and their corresponding integer values[span_0](start_span)[span_0](end_span)
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Traverse the string from back to front as suggested by the hint[span_1](start_span)[span_1](end_span)
        for char in reversed(s):
            current_value = roman_map[char]
            
            # If the current value is less than the previous, subtract it (e.g., IV, IX)
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
                
            prev_value = current_value
            
        return total