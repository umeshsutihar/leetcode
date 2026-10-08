class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def mergeSort(low: int, high: int) -> int:
            if low >= high:
                return 0
            
            mid = (low + high) // 2
            count = mergeSort(low, mid) + mergeSort(mid + 1, high)
            
            # Count reverse pairs
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
            
            # Merge the two sorted halves
            nums[low:high + 1] = sorted(nums[low:high + 1])
            return count

        return mergeSort(0, len(nums) - 1)


        
        