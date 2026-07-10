class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = [0] * n
        count = 0
        for i in range(n):
            if nums[i] != 0:
                temp[count] = nums[i]
                count += 1
        for i in range(count):
            nums[i] = temp[i]

        for i in range(count, n):
            nums[i] = 0   
        