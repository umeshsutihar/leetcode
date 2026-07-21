class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window_sum = 0
        max_sum = 0
        left = 0
        freq = {}

        for right in range(len(nums)):
            # Add current element
            window_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # Window size becomes k
            if right - left + 1 == k:

                # All elements must be distinct
                if len(freq) == k:
                    max_sum = max(max_sum, window_sum)

                # Remove left element
                window_sum -= nums[left]
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

        return max_sum