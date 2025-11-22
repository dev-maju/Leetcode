from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # for char in s:
        #     if char in t:
        #         return True
        #     elif char not in t:
        #         return False


        # return sorted(s)==sorted(t)


        # if Counter(s)!=Counter(t):
        #     return False
        # else:
        #     return True

        freq = [0] * 26

      
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1

        
        for count in freq:
            if count != 0:
                return False

        return True
