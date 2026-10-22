class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:


        d=Counter()
        d[0]=1
        ans=ex=0

        for val in nums:
            ex^=val
            ans+=d[ex]
            d[ex]+=1
        
        return ans
        