class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If the total sum required is greater than the maximum possible sum 
        # with 'num' digits (i.e., num * 9) or less than the minimum needed (0), return ""
        if sum < 0 or sum > 9 * num:
            return ""
        
        res = []
        rem_sum = sum
        rem_digits = num
        
        for i in range(num):
            rem_digits -= 1
            # We want the largest possible digit for the current position, 
            # but we must leave enough sum for the remaining digits.
            # Max possible for the rest is rem_digits * 9.
            # So, current digit cannot be less than rem_sum - rem_digits * 9.
            min_val = max(0, rem_sum - rem_digits * 9)
            max_val = min(9, rem_sum)
            
            # Since we want to maximize the score, we greedily pick the largest 
            # valid digit we can afford, which is max_val.
            digit = max_val
            res.append(str(digit))
            rem_sum -= digit
            
        return "".join(res)        