class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        ans = 0
        if x < 0:
            return False
        x1 = x
        x = abs(x)
        x = str(x)
        x = x[::-1]
        ans = int(x)
        if x1 == ans:
            return True
        else:
            return False



if __name__ == '__main__':
    nums = 12354321
    a = Solution()
    # print -1*nums
    print a.isPalindrome(nums)


