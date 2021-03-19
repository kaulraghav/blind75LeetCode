class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Base case/Edge case
        if not nums or len(nums) == 1:
            return False
        
        #Dict/Set Solution
        #Time: O(n)
        #Space: O(n)
        '''
        dict = {}
        
        for num in nums:
            if num not in dict:
                dict[num] = 0
            dict[num] += 1
            
        return any(x > 1 for x in dict.values())

        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
        '''
        #Sort solution
        #Time: O(nlogn)
        #Space: O(1)
        
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
