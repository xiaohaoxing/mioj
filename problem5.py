# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    list = []
    nums = line.split(",")
    for num in nums:
        list.append(int(num))
    length = len(list)
    for i in range(length - 1):
        if list[i] > list[i+1]:
            rotate_count = i + 1
            if rotate_count * 2 < length:
                return list[int(rotate_count + (length - 1) / 2)]
            else:
                return list[int(rotate_count - (length + 1) / 2)]

    return list[int((length + 1) / 2) - 1]


line = "12,13,14,5,6,7,8,9,10"
out = solution(line)
print(out)