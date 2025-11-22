class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for char in s:
        #     if char in t:
        #         return True
        #     elif char not in t:
        #         return False
        return sorted(s)==sorted(t)