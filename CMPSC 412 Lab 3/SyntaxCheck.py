# Ensure the syntax is correct of the input string.

import Stack


def SyntaxCheck(inputData):
    if inputData:
        stack1 = Stack.Stack()  # Creates a new empty stack.

        # Checks to make sure there is the correct amount of
        # symbols in the string and pushes and pops from
        # the stack to check.
        for i in inputData:
            if i == '{':
                stack1.push(i)
            elif i == '}':
                if stack1.pop() != '{':
                    return False
            elif i == '[':
                stack1.push(i)
            elif i == ']':
                if stack1.pop() != '[':
                    return False
            elif i == '(':
                stack1.push(i)
            elif i == ')':
                if stack1.pop() != '(':
                    return False
            else:
                continue
        if stack1.isEmpty():
            return True
        else:
            return False
    else:
        return False


print(SyntaxCheck("((())"))
print(SyntaxCheck("The { yes { more }} nice () best"))
