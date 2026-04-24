class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize hashmap
        hashmap = {}

        # loop through the array, enumerate gives index(i) and value(num)
        # check if the difference is in the hashmap
        # if it exists, return the indices of those values
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
        return False