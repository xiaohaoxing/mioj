

def solution(line):
    nums = line.split(',')
    count = 0
    for i in range(len(nums)):
        n = int(nums[i])
        left = nums[i+1:]
        count += left.count(str(10-n))
        count += left.count(str(n-10))
        count += left.count(str(n+10))
    return count


line = "6,4,16"
result = solution(line)
print(result)

