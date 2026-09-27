class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to keep binary search space O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len + 1) // 2

        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = half_len - i

            # Boundary values for partition comparison
            nums1_left_max = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right_min = nums1[i] if i < m else float('inf')

            nums2_left_max = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right_min = nums2[j] if j < n else float('inf')

            # Correct partition found
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if total_len % 2 == 1:
                    return float(max(nums1_left_max, nums2_left_max))
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0
            elif nums1_left_max > nums2_right_min:
                high = i - 1  # Too far right in nums1
            else:
                low = i + 1   # Too far left in nums1

        return 0.0
   