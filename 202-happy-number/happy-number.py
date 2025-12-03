def numNumber(n):
        num = 0
        while n :
            digit = n%10
            num = num + digit**2
            n=n//10
        return num
class Solution:
    
    
    def isHappy(self, n: int) -> bool:
        st = set()
        while 1:
            n = numNumber(n)
            if n==1:
                print(n)
                return True
            if n in st:
                print(n)
                return False
            st.add(n)

    