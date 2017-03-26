class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_prefx = ""
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            temp_char = strs[0][i]
            for j in range(len(strs)):
                if len(strs[j]) <= i:
                    return longest_prefx
                if strs[j][i] != temp_char:
                    return longest_prefx
            longest_prefx += temp_char
        return longest_prefx