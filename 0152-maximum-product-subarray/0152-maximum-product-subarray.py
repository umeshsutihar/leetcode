class Solution:
    def maxProduct(self, nums):
        curMax = nums[0]
        curMin = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                curMax, curMin = curMin, curMax

            curMax = max(num, curMax * num)
            curMin = min(num, curMin * num)

            ans = max(ans, curMax)

        return ans
        
        