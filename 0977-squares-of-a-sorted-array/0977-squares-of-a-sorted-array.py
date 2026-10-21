class Solution(object):
    def sortedSquares(self, nums):
        nums1 = [0] * len(nums)

        left = 0
        right = len(nums) - 1
        k = len(nums1) - 1

        while left <= right:
            if abs(nums[left])>abs(nums[right]):
                nums1[k] = nums[left] * nums[left]
                left+=1
                k-=1
            else:
                nums1[k] = nums[right] * nums[right]
                right-=1
                k-=1
            
        return nums1