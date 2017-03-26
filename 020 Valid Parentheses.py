class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if len(stack) != 0 and dic[s[i]] == stack[len(stack)-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack) != 0:
            return False
        else:
            return True
