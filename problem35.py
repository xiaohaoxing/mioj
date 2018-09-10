
# coding:utf-8


def solution(line):
    m,n = line.split(',')
    return split_num(int(m), int(n), int(m))

def split_num(m, n, ceil):
    """
    把一个数字 m 分成 n 个数字之和（包括0）
    """
    if m == 0:
        #如果已经放完了就只有一种(全是0)
        return 1
    if n == 1:
        #如果只有一个篮子就只有一种
        return 1
    #分为整除和非整除
    min_num = m/n
    min_int = int(m/n)
    if min_int != min_num:
        min_int += 1
    count = 0
    for i in range(min_int, m + 1):
        if i <= ceil:
            count += split_num(m - i, n - 1, i)
            print("共%d个鸡蛋，放%d个，后面%d个篮子放%d个鸡蛋"%(m, i, n-1, m-i))
    print("%d个鸡蛋放%d个篮子共%d种方法。(ceil=%d)"%(m, n, count, ceil))
    return count

line = "6,3"
result = solution(line)
print(result)
