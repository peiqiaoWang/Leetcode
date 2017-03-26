class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        k = 1
        size = len(nums)
        for i in range(1, size):
            if nums[k] == nums[k-1]:
                nums.pop(k)
                k -= 1
            k += 1
        return len(nums)
