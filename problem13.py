# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    nums_str, num_count = line.split(' ')
    nums = nums_str.split(',')
    counts = []
    for num in nums:
        n = int(num)
        exist = False
        for count in counts:
            if count.value == n:
                exist = True
                count.count += 1
        if not exist:
            counts.append(Node(n))
    counts.sort(key = lambda a:a.count*10-a.value, reverse=True)
    tops = counts[:int(num_count)]
    tops.sort(key = lambda a:a.value)
    result = ""
    for num in tops:
        result += str(num.value) + ','
    return result[:len(result)-1]

class Node:
    def __init__(self, num=-1):
        self.value = num
        self.count = 1

# def insert_list(list, node):
#     """
#     list 代表是头结点，node 代表是需要插入的节点。这里前提是：已经不能插入到list 这个节点的前面了。即：node 已经比 list 优先级低。
#     需要把 node 插入到 list 的后面紧邻一个才行。所以实际参与比较的是list.next。
#     :param list:
#     :param node:
#     :return:
#     """
#     neighbor = list.next
#     #list.next 没有
#     if neighbor == None:
#         list.next = node
#     else:
#         if neighbor.value == node.value:
#             insert_list(head, node)
#         #list.next 存在
#         if neighbor.count > node.count:
#             #neighbor 次数比 node 的大，继续向后找
#             insert_list(list.next, node)
#         elif neighbor.count == node.count:
#             #neighbor 和 node 的出现次数相同，比较value 大小了
#             if neighbor.value > node.value:
#                 list.insert_after(node)#当次数相同，且node 的数字比 neighbor 小，就直接在 list 后面
#             else:
#                 insert_list(list.next, node)#次数相同，但 node 比 neighbor 大，就继续向后找
#         else:
#             #neighbor 次数比 node 小，前提又是 list 确认在 node前面，就直接插入
#             list.insert_after(node)






line = "1,2,2,3,3 3"
result = solution(line)
print(result)