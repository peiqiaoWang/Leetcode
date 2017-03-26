class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10,
               'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = dic[s[0]]
        for i in range(1, len(s)):
            if dic[s[i]] > dic[s[i-1]]:
                ans += dic[s[i]] - 2*dic[s[i-1]]
            else:
                ans += dic[s[i]]
        return ans
if __name__ == '__main__':
    a = Solution()
    print a.romanToInt('VI')
