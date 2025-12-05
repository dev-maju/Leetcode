# def maxNum(nums, idx):
#     if idx == 0:
#         return 1
#     mx=1
#     for prev in range(idx):
#         if nums[prev] < nums[idx]:
#             mx = max(mx,maxNum(nums,prev)+1)
#     return mx
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         res=1
#         for idx in range(1,n):
#             res = max(res,maxNum(nums,idx))
#         return res

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[]
        import bisect
        for num in nums:
            pos = bisect.bisect_left(lis,num)
            if pos==len(lis):
                lis.append(num)
            else:
                lis[pos]=num
        return len(lis)
        