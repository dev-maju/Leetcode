class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for i in range(len(s)):
        #     if s.count(s[i])==1:
        #         return i
            
        
        # return -1

        
        freq = [0] * 26


        for ch in s:
            freq[ord(ch) - ord('a')] += 1

      
        for i in range(len(s)):
            if freq[ord(s[i]) - ord('a')] == 1:
                return i

        return -1          

                
                