

def solution(line):
    num = int(line)
    bin_num = bin(num)
    bin_str = str(bin_num)[2:].zfill(32)
    bin_str_re = "0b" + bin_str[::-1]
    return int(bin_str_re, 2)


line = "1"
result = solution(line)
print(result)