class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        # iterate through nums array, check for the difference
        # of target - index array
        for i in range(len(nums)):
            diff = target - nums[i]
            # if the difference is in hashmap, return index values that = target
            if diff in map:
                return [map[diff], i]
            # set index value of hashmap to the value in nums array
            map[nums[i]] = i

                

