class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k %=len(nums)
        # nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]
        # return nums

        
        k %= len(nums)

        def rev(a, l, r):
            while l < r:
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1

        rev(nums, 0, len(nums) - 1)
        rev(nums, 0, k - 1)
        rev(nums, k, len(nums) - 1)
