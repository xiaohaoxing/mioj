
def solution(line):
    stack = []
    for char in line:
        if char == '(':
            stack.append(char)
            continue
        elif char == '[':
            stack.append(char)
            continue
        elif char == '{':
            stack.append(char)
            continue
        elif char == ')':
            if len(stack) == 0:
                return '0'
            elif stack[len(stack)-1] == '(':
                stack.pop()
            else:
                return '0'
        elif char == ']':
            if len(stack) == 0:
                return '0'
            elif stack[len(stack)-1] == '[':
                stack.pop()
            else:
                return '0'
        elif char == '}':
            if len(stack) == 0:
                return '0'
            elif stack[len(stack)-1] == '{':
                stack.pop()
            else:
                return '0'
    if len(stack) == 0:
        return '1'
    else:
        return '0'

line = "[()]{}"
result = solution(line)
print(result)