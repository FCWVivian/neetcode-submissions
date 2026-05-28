class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0

        for t in tokens:
            print(stack, t)
            if t == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))
        print(stack)
        return int(stack[0])
        