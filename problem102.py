# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    result = line
    while(True):
        temp = result.replace("mi", "")
        if len(temp) == len(result):
            break
        result = temp
    return result


line = "abmmiicd"
result = solution(line)
print(result)