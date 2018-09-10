

def solution(line):
    tokens = line.split(' ')
    operator = []
    operands = []
    need_op = False
    for token in tokens:
        if token.isdigit():
            if need_op:
                #操作符是乘除，直接计算结果
                front = operands.pop()
                op = operator.pop()
                if (op == '/') & (token == '0'):
                    return 'err'
                if op == '*':
                    result = int(front) * int(token)
                elif op == '/':
                    result = int(int(front) / int(token))
                operands.append(result)
                need_op = False
            else:
                #加减就压入等后面的
                operands.append(token)
                need_op = False
        else:
            if token == '*' or token == '/':
                need_op = True
                operator.append(token)
            else:
                need_op = False
                operator.append(token)

    #最后计算所有加减
    while len(operator) > 0:
        op = operator.pop(0)
        num1 = operands.pop(0)
        num2 = operands.pop(0)
        if op == '+':
            result = int(num1) + int(num2)
        else:
            result = int(num1) - int(num2)
        operands.insert(0, result)
    return operands.pop()


line = "323 + 160 / 40 - 142"
result = solution(line)
print(result)