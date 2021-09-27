# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
from collections import deque


class MyNode:
    def __init__(self, value, letter=None, left=None, right=None):
        self.value = value
        self.letter = letter
        self.left = left
        self.right = right


def search(node, path=''):
    if node.letter is not None:
        node.value = 0
        return node.letter, path
    if node.right is not None and node.right.value != 0:
        cell = search(node.right, path=f'{path}1')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return cell
    if node.left is not None and node.left.value != 0:
        cell = search(node.left, path=f'{path}0')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return cell


def str_dict(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d


def make_tree():
    node_list = deque([MyNode(s_dict[i], i) for i in s_dict])
    for i in range(len(s_dict) - 1):
        node_list = deque(sorted(node_list, key=lambda node: node.value))
        first_el = node_list.popleft()
        second_el = node_list.popleft()
        new_node = MyNode(first_el.value + second_el.value, left=first_el, right=second_el)
        node_list.appendleft(new_node)
    tr = node_list[0]
    return tr


def get_table():
    tbl = {}
    for _ in range(len(s_dict)):
        k = search(tree)
        tbl[k[0]] = k[1]
    return tbl


def result():
    rslt = ''
    for _ in string:
        rslt = ''.join(table.values())
    print(string)
    print(rslt)


string = 'greek rode across the river'
s_dict = str_dict(string)
tree = make_tree()
table = get_table()
result()
