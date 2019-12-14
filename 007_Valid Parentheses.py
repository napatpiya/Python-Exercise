class Solution(object):
    def isValid(self, s):
        if s == '':
            return True
        elif len(s) % 2 == 1:
            return False

        stack = []

        left = ['(', '{', '[']
        right = [')', '}', ']']

        for letter in s:
            if letter in left:
                stack.append(letter)
            elif letter in right:
                if len(stack) <= 0:
                    return False
                else:
                    if left.index(stack.pop()) != right.index(letter):
                        return False
        
        return True

s1 = '()'
s2 = '([]())'
s3 = '(()((())))'
s4 = '[({})]'
s5 = '{([)][]}'
s6 = '{([](){()})}'

x = Solution()
print(x.isValid(s3))

