class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def backtrack(index, curr, curr_sum):
            if curr_sum == target:
                ans.append(curr[:])
                return
            if curr_sum > target or index == len(candidates):
                return

            
            curr.append(candidates[index])
            backtrack(index, curr, curr_sum + candidates[index])
            curr.pop()

            backtrack(index + 1, curr, curr_sum)

        backtrack(0, [], 0)
        return ans
        