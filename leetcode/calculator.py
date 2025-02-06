class Solution:
    def operate(self, s):
        i = len(s) - 1
        number = 0
        while i >= 0:
            if s[i] == "(":
                i -= 1
            elif s[i] == "+":
                number += int(s[i - 1])
                i -= 2
            elif s[i] == "-":
                number -= int(s[i - 1])
                i -= 2
            else:
                number += int(s[i])
                i -= 1
        return number

    def calculate(self, s: str) -> int:
        stack = []
        operation = []
        iterator = 0
        while iterator < len(s):
            number = s[iterator]
            if number == " ":
                iterator = iterator + 1
                continue
            if number == ')':
                value = None
                while value != '(':
                    value = stack.pop()
                    operation.append(value)
                sum_val = self.operate(operation)
                stack.append(sum_val)
                operation = []
            elif s[iterator].isdigit():
                n = 0
                number = 0
                while iterator < len(s) and s[iterator].isdigit():
                    number = int(s[iterator]) + number * 10
                    n += 1
                    iterator += 1
                iterator -= 1
                stack.append(str(number))
            else:
                stack.append(number)
            iterator += 1
        while len(stack) > 0:
            operation.append(stack.pop())
        return self.operate(operation)

