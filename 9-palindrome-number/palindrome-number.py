# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         reverse = 0
#         temp = abs(x)
#         if x< 0:
#             return False
#         while temp!=0:
#             reverse = (reverse*10)+(temp%10)
#             temp = temp//10
#         return (reverse==abs(x))

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10