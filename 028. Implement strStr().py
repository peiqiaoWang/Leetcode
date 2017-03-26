class Solution(object):

    def get_prexlong(self, needle):
        self.next = []
        self.next.append(-1)
        j = -1
        i = 0
        size = len(needle)
        while i < size:
            while j != -1 and needle[i] != needle[j]:
                j = self.next[j]
            i += 1
            j += 1
            self.next.append(j)
        print self.next

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        i = 0
        j = 0
        if needle == "":
            return 0
        if n < m:
            return -1
        self.get_PrexLong(needle)
        while i < n:
            while j != -1 and haystack[i] != needle[j]:
                j = self.next[j]
            i += 1
            j += 1
            if j == m:
                return i-m
        return -1

if __name__ == "__main__":
    a = Solution()
    print a.strStr("mississippi", "issip")

