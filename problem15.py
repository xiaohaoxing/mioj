
def solution(line):
    nums = line.split(',')
    all_result = []
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if int(nums[i])+int(nums[j])+int(nums[k]) == 0:
                    group = [int(nums[i]), int(nums[j]), int(nums[k])]
                    all_result.append([max(group), min(group)])
    #开始去重
    for source in all_result:
        exist = False
        for target in result:
            if target == source:
                exist = True
        if not exist:
            result.append(source)
    return len(result)


line = "-1,0,1,2,-1,-4"
result = solution(line)
print(result)
