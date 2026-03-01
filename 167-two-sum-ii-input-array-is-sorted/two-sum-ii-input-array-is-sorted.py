class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}
        for i,n in enumerate(numbers):
            diff = target - n
            if diff in hashset:
                return [hashset[diff]+1,i+1]
            hashset[n] = i
        return