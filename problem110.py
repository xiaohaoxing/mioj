
def solution(line):
    num_p, p, q = line.split(' ')
    #计算出 base 10的数字
    num_10 = 0;
    p = int(p)
    for char in num_p:
        num_10 *= p
        if char == 'a':
            num_10 += 10
        elif char == 'b':
            num_10 += 11
        elif char == 'c':
            num_10 += 12
        elif char == 'd':
            num_10 += 13
        elif char == 'e':
            num_10 += 14
        elif char == 'f':
            num_10 += 15
        else:
            num_10 += int(char)
    #转化为 q 进制的
    q = int(q)
    reminder = num_10
    num_q = ''
    while(reminder > 0):
        digit = reminder % q
        reminder = int(reminder / q)
        num_q = get_num_char(digit) + num_q
    return num_q

def get_num_char(num):
    if num == 10: return 'a'
    elif num == 11: return 'b'
    elif num == 12: return 'c'
    elif num == 13: return 'd'
    elif num == 14: return 'e'
    elif num == 15: return 'f'
    else: return str(num)



line = "31 10 16"
result = solution(line)
print(result)