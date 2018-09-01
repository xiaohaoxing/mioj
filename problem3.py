# 此处可 import 模块
########
#Accept#
########
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    a, tmp, b = line.split()
    size1 = len(a)
    size2 = len(b)
    result = []
    borrow = False  # 是否需要借位
    digit = 1  # 当前位置。1代表个位。
    # 处理2个相减
    while (digit <= size2):
        minuser = int(a[size1 - digit])
        minusee = int(b[size2 - digit])
        if borrow:
            minuser -= 1
        if minuser < minusee:
            borrow = True
            minuser = minuser + 10
        else:
            borrow = False
        result.append(str(minuser - minusee))
        digit += 1
    # 处理被减数最高位的借位
    if borrow:
        result.append(str(int(a[size1 - digit]) - 1))
    else:
        result.append(a[size1 - digit])
    digit += 1
        # 处理减数最后的高位
    while (digit <= size1):
        result.append(a[size1 - digit])
        digit += 1

    result.reverse()
    result = str(int("".join(result)))

    # 返回处理后的结果
    return result


line = "1231231237812739878951331231231237812739878951331231231237812739878951331231231237812739878951331231231237812739878951331231231237812739870 - 89513312312312378127398789513312312312378127398789513312312312378127398789513"
line2 = "123 - 26"
result = solution(line2)
print(result)