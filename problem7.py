# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    char_list = line.split(',')
    #先找最大的正数
    max = 0
    for i in char_list:
        num = int(i)
        if num > max:
            max = num
    bucket = list(range(max+1))
    for i in range(max+1):
        bucket[i] = 0
    for i in char_list:
        num = int(i)
        if num > 0:
            bucket[num] = 1
    for i in range(1, max+1):
        if bucket[i] == 0:
            return i
    return max + 1

line = "3,-1,1,2,5"
result = solution(line)
print(result)