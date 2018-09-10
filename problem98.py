
def solution(line):
    nums = line.split(' ')
    nums.sort(key=lambda x: int(x), reverse=True)

    for i in range(len(nums)):
        nums[i] = int(nums[i]) * (i + 1)
    return max(nums)


line = "5 0 29 14"
result = solution(line)
print(result)