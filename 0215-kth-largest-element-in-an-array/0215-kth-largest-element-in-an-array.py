class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        pq = []

        for i in range(k):
            heapq.heappush(pq, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > pq[0]:
                heapq.heappushpop(pq, nums[i])

        return pq[0]
