class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1,n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp
    #     ad = []
    #     for i in range(n+1):
    #         ad.append(self.add(i))
    #     return ad

    # def add(self, i):
    #     res = 0 
    #     while i:
    #         if i%2 == 1:
    #             res+=1
    #         i = i//2
    #     return res