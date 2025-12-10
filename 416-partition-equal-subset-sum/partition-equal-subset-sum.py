# def isSubsetSum(n,arr,sum):
#     if sum ==0:
#         return True
#     if n==0:
#         return False
    
#     if arr[n-1]>sum:
#         return isSubsetSum(n-1,arr,sum)
    
#     return isSubsetSum(n-1,arr,sum) or  isSubsetSum(n-1,arr,sum - arr[n-1])

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         arrSum = sum(nums)
#         if arrSum%2 != 0:
#             return False
#         return isSubsetSum (len(nums),nums,arrSum//2)

# from typing import List

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         # odd total cannot be partitioned into two equal subsets
#         if total % 2 != 0:
#             return False

#         target = total // 2
#         # dp[t] = whether a subset sum t is possible
#         dp = [False] * (target + 1)
#         dp[0] = True

#         for num in nums:
#             # iterate backwards to avoid reusing the same number
#             for t in range(target, num - 1, -1):
#                 if dp[t - num]:
#                     dp[t] = True
#             if dp[target]:
#                 return True   # early exit

#         return dp[target]


from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        bits = 1  # bit 0 set -> sum 0 is possible
        for num in nums:
            bits |= (bits << num)         # shift the bitset by num and OR
            # optional early exit:
            if (bits >> target) & 1:
                return True

        return ((bits >> target) & 1) == 1
