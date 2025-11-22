class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_sum=nums[0]
        # curr_sum=0
        # for i in nums:
        #     if curr_sum<0:
        #         curr_sum=0
        #     curr_sum+=i
        #     max_sum=max(max_sum,curr_sum)
        # return max_sum

        curr=0
        best=nums[0]
        for x in nums:
            curr=x if curr < 0 else curr+x
            best=best if best>curr else curr
        return best
            
           
            

