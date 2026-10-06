class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        running = nums[0]
        output.append(running)
        for i in range (1,len(nums)):
            running = nums[i]+ running  

            output.append(running)
        return output

        

            