class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        numSet = set(nums)
        longest = 0
        
        for num in numSet:
            
            if num - 1 not in numSet:
                current = num
                count = 1
                
                while current + 1 in numSet:
                    current += 1
                    count += 1
                
                longest = max(longest, count)
        
        return longest
        