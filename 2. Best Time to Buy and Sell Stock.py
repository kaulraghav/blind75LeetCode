import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Base case/Edge case
        if not prices:
            return 0
        
        #Brute force
        #Time: O(n^2)
        #Space: O(1)
        '''
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                maxProfitSeen = max(maxProfitSeen, profit)
                
        return maxProfitSeen
        '''
        
        #LeetCode solution
        #Time: O(n) Traverse prices once
        #Space: O(1) constant
        
        minPrice = math.inf
        maxProfit = 0
        
        for price in prices:
            #If this statement doesn't satisfy we don't update maxProfit
            #since it'll either remain 0 or go negative so no point updating
            if price < minPrice:
                minPrice = price
            #Does not update maxProfit everytime (hence elif instead of else)
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice
        
        return maxProfit
