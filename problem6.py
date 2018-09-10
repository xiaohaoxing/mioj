# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    a, b, c = line.split(",")
    result = digest_one(a, b, c)
    if result:
        return "true"
    else:
        return "false"


def digest_one(feeder1, feeder2, target):
    #一个串已经到头了，直接比较另一个串和目标就行了
    if len(feeder1) == 0:
        if feeder2 == target:
            return True
        else:
            return False
    if len(feeder2) == 0:
        if feeder1 == target:
            return True
        else:
            return False

    can1 = can_digest(feeder1, target)
    can2 = can_digest(feeder2, target)
    #2个串都可以，则需要回溯
    if can1 & can2:
        return digest_one(feeder1[1:], feeder2, target[1:]) | digest_one(feeder1, feeder2[1:], target[1:])
    #仅串1可以匹配
    elif can1:
        return digest_one(feeder1[1:], feeder2, target[1:])
    elif can2:
        return digest_one(feeder1, feeder2[1:], target[1:])
    else:
        return False

def can_digest(feeder, target):
    if feeder[0] == target[0]:
        return True
    else:
        return False



result = solution("abc,bca,aabbcc")
print(result)