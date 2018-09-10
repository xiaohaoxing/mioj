
def solution(line):
    m = []
    rows = line.split(';')
    for row in rows:
        m.append(row.split(','))
    max = int(m[0][0]) + int(m[1][1])
    for i in range(len(m) - 1):
        for j in range(len(m[0]) - 1):
            current = int(m[i][j]) + int(m[i+1][j+1])
            if current > max:
                max = current
    return max


line = "3,3,1,3,4;5,5,7,10,1;2,9,5,3,3"
result = solution(line)
print(result)