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

        
        # clean = ''
        # for char in s:
        #     if char.isalnum():
        #         clean += char.lower()
        
        # rev = clean[::-1]
        # return clean == rev

        
        # s = ''.join(c.lower() for c in s if c.isalnum())
        # return s == s[::-1]


        


