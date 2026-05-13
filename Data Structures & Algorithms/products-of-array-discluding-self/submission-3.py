class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #   [1,2,4,6]
        # [1,1,2,8,48,48]
        # [1,48,48,24,6,1]
        
        # [1,48,24,12,8,1]
        prefix_multip = [1] * (len(nums) + 2)
        suffix_multip = [1] * (len(nums) + 2)
        for i in range(len(nums)): #  [0,4)
            prefix_multip[i + 1] = prefix_multip[i] * nums[i]
            suf_index = len(suffix_multip) - 2 - i
            # suffix_multip[4] = suffix_multip[5] * nums[3] = 6
            # suffix_multip[]
            suffix_multip[suf_index] = suffix_multip[suf_index + 1] * nums[len(nums) - 1 - i]   
        return [prefix_multip[i] * suffix_multip[i + 2] for i in range(len(nums))]
                    
        