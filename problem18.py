import json

def solution(line):
    json_line = json.loads(line)
    json_line.sort(key=lambda x: x[1], reverse=False)
    json_line.sort(key=lambda x: x[0], reverse=True)
    result = []
    for stu in json_line:
        pos = stu[1]
        result.insert(pos, stu)
    return str(result).replace(" ", "")


line = "[[7,0],[4,4],[7,1],[5,2],[6,1],[5,0]]"
result = solution(line)
print(result)