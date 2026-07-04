class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        if len(t) != len(s):
            return False
        
        for ch in s:
            if ch  in hash_map:
                hash_map[ch] += 1
            
            else:
                hash_map[ch] = 1
            
        for ch in t:
            if ch  not in hash_map:
              
                return False
            hash_map[ch] -= 1
        
        for value in hash_map.values():
            if value != 0:
                return False
            
            
             

        return True
    

        

        
        