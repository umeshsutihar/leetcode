class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        max_result = float('-inf')
        left = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            if(right-left + 1) == k:
                max_result = max(max_result, window_sum)
                window_sum -= nums[left]
                left += 1
        return max_result / k