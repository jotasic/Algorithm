#https://leetcode.com/problems/two-sum/

#Runtime: 48 ms, faster than 62.52% of Python3 online submissions for Two Sum.
#Memory Usage: 14.5 MB, less than 45.84% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arrLen =  len(nums) 
        for i in range(0, arrLen-1) :
            for j in range(1, arrLen) :
                if i == j :
                    continue

                sumValue = nums[i] + nums[j]
                if sumValue == target :
                    return [i, j]
                    