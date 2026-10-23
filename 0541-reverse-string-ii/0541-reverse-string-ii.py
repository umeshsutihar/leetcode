class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        n = len(chars)
 
        for start in range(0, n, 2 * k):
            i = start
            j = min(start + k - 1, n - 1)

            while i < j:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
                
        return "".join(chars)

        