class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for j in range(0,len(nums)):
            count = 0
            for i in range(0,len(nums)):
                if nums [i] == nums[j]:
                    count+=1
            if count >1:
                return True
            
        return False