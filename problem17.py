#encoding=utf8
# coding:utf-8
def solution(line):
    line = line.encode("utf8")
    digits = len(line)
    #计算出有几个部
    piece_count = int(digits/4)
    if piece_count != float(digits)/4:
        piece_count += 1
    full_line = line.zfill(piece_count * 4)
    pieces = []
    while(len(full_line)>0):
        pieces.append(full_line[:4])
        full_line = full_line[4:]

    #4位以下
    if len(pieces) == 1:
        temp = piece_trans(pieces[0], False)
        return ('零' if temp == '' else temp)+'元整'
    elif len(pieces) == 2:
        return piece_trans(pieces[0], False) + '万' + piece_trans(pieces[1], True) + '元整'
    elif len(pieces) == 3:
        #对上亿的还要对万处理
        temp = piece_trans(pieces[1], True)
        return piece_trans(pieces[0], False) + '亿' + temp + ('' if temp == '' else '万') + piece_trans(pieces[2], True) + '元整'
    else:
        print('数字太大啦！')


def piece_trans(piece, leader):
    '''
    这里仅转化4位的结果
    '''
    if len(piece) != 4:
        return ''
    result = ''
    forth = int(piece[0])
    third = int(piece[1])
    second = int(piece[2])
    first = int(piece[3])
    blank = False
    if forth > 0:
        result += char_trans(forth)+'仟'
    elif leader:
        result += '零'

    if third > 0:
        result += char_trans(third) + '佰'
    elif not result.endswith('零'):
        result += '零'

    if second > 0:
        result += char_trans(second) + '拾'
    elif not result.endswith('零'):
        result += '零'

    if first > 0:
        result += char_trans(first)
    elif result.endswith('零'):
        #个位还是0，那么中文就不需要零结尾了。
        while(result.endswith('零')):
            result = result[0:len(result)-3]
    if not leader:
        while(result.startswith('零')):
            result = result[3:len(result)]
    return result


def char_trans(char):
    '''
    这里仅转化1个数字到汉字
    '''
    if char == 1: return '壹'
    if char == 2: return '贰'
    if char == 3: return '叁'
    if char == 4: return '肆'
    if char == 5: return '伍'
    if char == 6: return '陆'
    if char == 7: return '柒'
    if char == 8: return '捌'
    if char == 9: return '玖'
    else:print(char + '转化出现问题啦：')

line = '8900000000'
result = solution(line)
print(result)


"""
捌拾玖亿元整
230
141
140
230
139
190
231
142
150
228
186
191
229
133
131
230
149
180

��捌拾玖亿�万�元整
155  !
182  !
230
141
140
230
139
190
231
142
150
228
186
191
233  !
155  !
228  !
184  !
135  !
233  !
155  !
229
133
131
230
149
180
"""
