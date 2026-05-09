class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = set()
        for item in nums:
            if item in has:
                return True
            has.add(item)    
        return False        
