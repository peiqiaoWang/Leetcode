class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        size = len(nums)
        for i in range(size):
            hashTable[nums[i]] = i
        for i in range(size):
            num = target-nums[i]
            if hashTable.get(num) != None and hashTable.get(num) != i:
                return [i, hashTable.get(num)]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    a = Solution()
    print a.twoSum(nums, target)
