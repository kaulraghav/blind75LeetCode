#Complexity
#Time: O(n) Traversing nums once
#Space: O(n) Worst case if no target found

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Base case/ Edge case
        if not nums:
            return []
        dict = {} # in the form {number : index}
        
        for i in range(len(nums)):
            #If difference is present in dict
            if target - nums[i] in dict:
                return [i, dict[target - nums[i]]]
            else:
                dict[nums[i]] = i
                
        #If no target pair found                 
        return -1
