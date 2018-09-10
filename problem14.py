

def solution(line):
    list_str, target = line.split(' ')
    list = list_str.split(',')
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1