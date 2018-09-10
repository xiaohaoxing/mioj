# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    target, source = line.split(' ')
    char_list = list(source)
    for i in target:
        try:
            char_list.remove(i)
        except:
            return "false"
    return "true"

