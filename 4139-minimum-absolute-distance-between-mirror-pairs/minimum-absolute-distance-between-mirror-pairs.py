class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # hashset = {}
        # def rev(i):
        #     rev=0
        #     while i:
        #         rev = rev*10 + (i%10)
        #         i//=10
        #     return int rev
        # minDist = float('inf')
        # for i in range(len(nums)):
        #     reverse = rev(nums[i])
        #     if reverse in hashset:
        #         minDist = min(minDist, abs(i-hashset[reverse]))
        #     hashset[nums[i]] =i
        # return minDist if minDist!=float('inf') else -1
            

        # hashset = {}
        # def rev(x):
        #     return int(str(x)[::-1])
        
        # ans = float('inf')
        # for i, x in enumerate(nums):
        #     reverse = rev(x)
        #     if reverse in hashset:
        #         ans = min(ans, abs(i-hashset[reverse]))
        #     hashset[x] = i
        
        # return ans if ans!= float('inf') else -1

        from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        mp = {}  # stores reversed value -> index
        ans = float('inf')

        for i, x in enumerate(nums):
            # Check if current number matches any previously stored reverse
            if x in mp:
                ans = min(ans, i - mp[x])
                if ans == 1:   # best possible answer
                    return 1

            # Store reverse of current number
            rev = int(str(x)[::-1])
            mp[rev] = i

        return -1 if ans == float('inf') else ans