# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
count = 0
def solution(line):
    nums, target = line.split(' ')
    char_list = nums.split(',')
    get_sum(char_list, target)
    return count

def get_sum(nums, target):
    global count
    for num in nums:
        if num == target:
            count += 1
        elif num < target:
            get_sum(nums, str(int(target)-int(num)))


line = "1,2,3 4"
result = solution(line)
print(result)