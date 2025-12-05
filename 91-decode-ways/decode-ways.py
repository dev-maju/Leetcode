# def decodeHelper(digits, index):
#     n = len(digits)
#     if index >= n:
#         return 1

#     ways=0
    
#     if digits[index] != '0':
#         ways=  decodeHelper(digits, index+1)
    
#     if (index+1<n and ((digits[index] == '1' and digits[index+1] <= '9') or
#     (digits[index]=='2' and digits[index+1]<='6' ))):
#         ways += decodeHelper(digits,index+2)
    
#     return ways


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         return decodeHelper(s,0)

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            if s[i] == '0':
                return 0

            # decode single digit
            ways = dfs(i + 1)

            # decode two digits
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                ways += dfs(i + 2)

            memo[i] = ways
            return ways

        return dfs(0)