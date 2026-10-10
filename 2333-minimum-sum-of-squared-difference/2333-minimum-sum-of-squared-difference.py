class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        from collections import Counter
        
        total_k = k1 + k2
        
        # Calculate absolute differences and count their frequencies
        diff_counts = Counter(abs(a - b) for a, b in zip(nums1, nums2))
        
        # If total operations needed is less than or equal to sum of all differences, we can reduce everything to 0
        if sum(diff_counts.values()) <= total_k and sum(d * c for d, c in diff_counts.items()) <= total_k:
            return 0
            
        # Get unique differences sorted in descending order
        unique_diffs = sorted(diff_counts.keys(), reverse=True)
        
        # Greedily reduce the largest differences
        for i, d in enumerate(unique_diffs):
            if d == 0:
                break
            count = diff_counts[d]
            # Next smaller difference value
            next_d = unique_diffs[i + 1] if i + 1 < len(unique_diffs) else 0
            
            # The total decrease we can make on all elements of value `d` to bring them down to `next_d`
            diff_height = d - next_d
            total_operations_needed = diff_height * count
            
            if total_k >= total_operations_needed:
                total_k -= total_operations_needed
                diff_counts[d] = 0
                diff_counts[next_d] += count
            else:
                # We can partially reduce these elements
                full_steps = total_k // count
                remainder = total_k % count
                
                diff_counts[d] -= count
                diff_counts[d - full_steps] += count - remainder
                diff_counts[d - full_steps - 1] += remainder
                total_k = 0
                break
                
        ans = 0
        for d, count in diff_counts.items():
            ans += (d ** 2) * count
            
        return ans