from typing import List
class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        ### Brute Force Approach o(n^3)

        # result = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 a = [nums[i], nums[j], nums[k]]
        #                 a.sort()
        #                 if a not in result:
        #                     result.append(a)
        #                 continue
        # return result

        ### Improved Brute Force Approach 
        result=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i >0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            for j in range(i+1,len(nums)-1):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                if nums[i]+nums[j]>0:
                    break
                for k in range(j+1,len(nums)):
                    if k>j+1 and nums[k]==nums[k-1]:
                        continue
                    if nums[i]+nums[j]+nums[k]==0:
                        result.append([nums[i],nums[j],nums[k]])
                    elif nums[i]+nums[j]+nums[k]>0:
                        break
        return result