class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif i == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == '-':
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(a - b)
            elif i == '/':
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(a / b)
            else:
                stack.append(i)
        return int(stack[0])