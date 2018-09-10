def solution(line):
    if line.count('+') > 0:
        a,b = line.split('+')
        result = 0
        a_r = a[::-1]
        b_r = b[::-1]
        sum_digit = min(len(a_r), len(b_r))
        level = 1
        for i in range(sum_digit):
            x = int(a_r[i])
            y = int(b_r[i])
            result = result + (x + y) * level
            level *= 10
        if len(a_r) > sum_digit:
            for d in a_r[sum_digit:]:
                result = result + int(d) * level
                level *= 10
        else:
            for d in b_r[sum_digit:]:
                result = result + int(d) * level
                level *= 10
        return result
    elif line.count('<') > 0:
        small, big = line.split('<')
    elif line.count('>') > 0:
        big, small = line.split('>')
    if len(big) > len(small):
        return 'Y'
    if len(big) < len(small):
        return 'N'
    for i in range(len(big)):
        if big[i] > small[i]:
            return 'Y'
        if big[i] < small[i]:
            return 'N'
    return 'N'
