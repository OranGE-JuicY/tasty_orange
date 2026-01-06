class Solution:
    def twoSum_doubleloop(self, nums:list[int], target: int)-> list[int]:
        # Brute force approach
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_hashtable(self, nums:list[int], target: int)-> list[int]:
        # Hashtable approach
        hash_table = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_table:
                return [hash_table[complement], i]
            # store the index as value and the number as key
            hash_table[num] = i