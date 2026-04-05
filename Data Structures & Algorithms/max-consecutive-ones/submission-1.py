class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = []
        for i in range(0,len(nums)):
            count = 0
            if nums[i] == 1:
                count+=1
                for j in range(i+1,len(nums)):
                    if nums[j] == 1:
                        count+=1
                    else:
                        break
            counter.append(count)
        max = counter[0]
        for i in range(1,len(counter)):
            if counter[i] > max:
                max = counter[i]

        return max