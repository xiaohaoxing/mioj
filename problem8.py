# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    char_list = line.split(',')
    count = 0
    #是否需要再遍历一次
    need_check = True
    while(need_check):
        need_check = False
        for i in range(len(char_list) - 1):
            current = int(char_list[i])
            next = int(char_list[i+1])
            if current > next:
                swap(char_list, i)
                count += 1
                need_check = True
    return count


def swap(list, pos):
    left = list[pos]
    right = list[pos + 1]
    list[pos] = right
    list[pos + 1] = left


line = "4,2,3,1"
result = solution(line)
print(result)