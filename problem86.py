def solution(line):
    num = int(line)
    power = 1
    rule1 = False
    rule2 = False
    while(power < num + 2):
        if num == power + 1:
            rule1 = True
        if num == power - 1:
            rule2 = True
        power = power * 2
    if rule1 and rule2:
        return "Very Good"
    elif rule1 and (not rule2):
        return "Good"
    elif (not rule1) and rule2:
        return "Bad"
    else:
        return "Normal"

line = "8"
result = solution(line)
print(result)