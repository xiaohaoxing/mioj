# 此处可 import 模块
import time
import datetime
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    str, k = line.split(' ')
    result = getMin(str, int(k))
    return int(result)


def getMin(str, k):
    """
    给定 str 是个数字串，需要移除其中的 K 个得到最小的数字串。
    """
    if k >= len(str):
        return 0
    if k == 1:
        if str[1] == '0':
            return int(str[1:])
        else:
            #直接移除最大的一个就完事了
            largest = max(str)
            a, b = str.split(largest, 1)
            return int(a + b)
    else:
        result_list = []
        for i in range(len(str)):
            result_list.append(getMin(str[0:i]+str[(i+1):len(str)], k-1))
        return min(result_list)


start = datetime.datetime.now()
line = "1432219 3"
result = solution(line)
print(result)
end = datetime.datetime.now()
print("运行了：" + str(end-start) + "s")