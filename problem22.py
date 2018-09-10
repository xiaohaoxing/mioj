def solution(line):
    num = int(line)
    current_length = 1
    while(current_length < num):
        num -= current_length
        current_length += 1

    print("第%d个子串的第%d个元素"%(current_length, num))
    tmp = '12345678987654321';
    return tmp[(num-1)%17]

