class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=''
        flag=0
        for char in s:
            if char.isalnum():
                clean+=char
        if clean.lower() == clean.lower()[::-1]:
            return True
        else:
            return False
        


