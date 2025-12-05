class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        temp = abs(x)
        if x< 0:
            return False
        while temp!=0:
            reverse = (reverse*10)+(temp%10)
            temp = temp//10
        return (reverse==abs(x))