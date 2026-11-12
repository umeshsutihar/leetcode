class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        rsum = 0
        
        for i in range(k):
            lsum += cardPoints[i]
        
        maxsum = lsum
        rightIndex = len(cardPoints) - 1

        for i in range(k - 1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rightIndex]
            rightIndex -= 1
            maxsum = max(maxsum, lsum + rsum)   
            
        return maxsum