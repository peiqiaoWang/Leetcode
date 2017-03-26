class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        size = len(nums)
        for i in range(size):
            if nums[k] == val:
                nums.pop(k)
                k -= 1
            k += 1
        return k

if __name__ == '__main__':
    a = Solution()
    print a.removeElement([3,2,2,2,3], 2)