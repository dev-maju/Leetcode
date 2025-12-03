# def numNumber(n):
#         num = 0
#         while n :
#             digit = n%10
#             num = num + digit**2
#             n=n//10
#         return num
# class Solution:
    
    
#     def isHappy(self, n: int) -> bool:
#         st = set()
#         while 1:
#             n = numNumber(n)
#             if n==1:
#                 print(n)
#                 return True
#             if n in st:
#                 print(n)
#                 return False
#             st.add(n)

class Solution:
    def getNext(self, n: int) -> int:
        total = 0
        while n:
            n, d = divmod(n, 10)
            total += d * d
        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.getNext(n)

        # Floyd's cycle detection
        while fast != 1 and slow != fast:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

        return fast == 1
    