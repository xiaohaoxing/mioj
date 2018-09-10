# 此处可 import 模块
#爬楼梯


def solution(line):
    num = int(line)
    return get_count(num)


def get_count(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return get_count(num - 1) + get_count(num - 2)


result = solution(10)
print(result)
