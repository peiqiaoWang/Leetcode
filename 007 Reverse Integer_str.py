class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        ans = 0
        if x >= 0:
            sign = 0
        elif x < 0:
            sign = 1
        x = abs(x)
        x = str(x)
        x = x[::-1]
        ans = int(x)
        if ans > INT_MAX or ans < INT_MIN:
            return 0
        elif sign == 1:
            return -1*ans
        else:
            return ans


if __name__ == '__main__':
    nums = -4321515
    a = Solution()
    print -1*nums
    print a.reverse(nums)


