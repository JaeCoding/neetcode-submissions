class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        save = {}
        for i in range(len(nums)):
            save[nums[i]] = i 
        for j in range(len(nums)):
            if target - nums[j] in save and j != save[target - nums[j]]:
                return [j, save[target - nums[j]]]
        return None        
        