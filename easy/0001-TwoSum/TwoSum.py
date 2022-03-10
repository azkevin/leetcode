from typing import List

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numsToIndex:
                return [numsToIndex[target - nums[i]], i]
            numsToIndex[nums[i]] = i

    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def twoSumBF(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i, j]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum([3,3], 6))