def solution(line):
    nums = line.split(',')
    dict = {}
    for num in nums:
        if dict.get(num) is not None:
            dict[num] += 1
        else:
            dict[num] = 1

    for key, value in dict.items():
        if value == 1:
            return key



