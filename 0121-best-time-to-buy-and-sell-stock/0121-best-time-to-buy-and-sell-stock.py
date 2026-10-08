class Solution(object):
    def maxProfit(self, prices):
        j = 0 
        maximum_profit = 0
        for i in range (1,len(prices)):
            if prices[i]<prices[j]:
                j = i
            x =  prices[i]-prices[j]
            if x> maximum_profit:
                maximum_profit = x
        return maximum_profit