class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(':')',
            '{':'}',
            '[':']'
        }

        stack = []

        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if stack == []:
                    return False
                if i != mapping[stack.pop(-1)]:
                    return False
        return stack == []