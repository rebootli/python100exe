
# region 生成式（推导式）的用法


# prices ={
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29    
# }

# prices2 = {key: value for key , value in prices.items() if value >100}
# print(prices2)


#endregion



# region 嵌套列表
'''
names = ['张三','李四','王五','赵六','哈七']
courses =['chinese','math','english']

# [None] * len(courses)：创建一个长度为 len(courses) 的列表，列表中的每个元素都是 None。
# 例如，如果 courses 列表有 3 个元素，那么 [None] * len(courses) 就会生成 [None, None, None]。
scores = [[None] * len(courses) for _ in range(len(names))]

# enumerate 是 Python 内置函数，它会将一个可迭代对象（如列表、元组等）组合为一个索引序列，同时列出数据和数据的索引。
# 在这个例子中，enumerate(names) 会返回一个包含索引和对应学生姓名的元组，例如 (0, '张三')、(1, '李四') 等。
# row 是索引，name 是学生姓名。
for row,name in enumerate(names):
    for col,course in enumerate(courses):
        scores[row][col] = float(input(f'please input{name}的 {course}成绩：'))
print(scores)
'''

# 如果不使用 enumerate 函数，要获取元素的索引就需要额外定义一个变量来记录当前的索引位置，
# 这会让代码变得更复杂。而使用 enumerate 函数，代码会更简洁明了。
'''
names = ['张三','李四','王五','赵六','哈七']
courses =['chinese','math','english']
scores = [[None] * len(courses) for _ in range(len(names))]
row = 0
for name in names:
    col = 0
    for course in courses:
        scores[row][col] = float(input(f'please input{name}的 {course}成绩：'))
        col = col + 1
    row = row + 1
print(scores)
'''

# 当没有enumerate，且又不用row和col，那么就无法以多元列表的下表赋值，
# scores就变成只有一个最后录入的值的列表
'''
names = ['张三','李四']
courses =['chinese','math']
scores = []

for name in names:
    for course in courses:
        scores = float(input(f'please input{name}的 {course}成绩：'))
print(scores)
'''

# endregion



# region  heapq模块（堆排序）


# 从列表中找出最大的或最小的N个元素
# 堆结构(大根堆/小根堆)

'''
import heapq

list1 = [34,25,12,99,87,63,58,78,88,92]
list2 = [
    {'name':'IBM','shares':100,'price':91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(heapq.nlargest(3,list1))
print(heapq.nsmallest(3,list1))
print(heapq.nlargest(2,list2,key=lambda x: x['price']))
print(heapq.nlargest(2,list2,key=lambda x: x['shares']))
'''
# endregion



# region itertools模块
'''迭代工具模块'''
'''
import itertools 

# 产生ABCD的全排列
result1 = itertools.permutations('ABCD')
# 打印前几个排列
for i, perm in enumerate(result1):
    if i < 5:
        print(''.join(perm))


# 产生ABCDE的五选三组合
result2 = itertools.combinations('ABCDE',3)
# 打印所有组合
for comb in result2:
    print(''.join(comb))


# 产生ABCD和123的笛卡尔积
result3 = itertools.product('ABCD','123')
# 打印所有组合
for product in result3:
    print(''.join(product))


# 产生ABC的无限循环序列
result4 = itertools.cycle(('A','B','C'))
# 打印前 5 个元素
for i in range(5):
    print(next(result4))
'''
# endregion



# region collections模块


#找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))
"""
# endregion




# region 排序算法（选择、冒泡和归并）和查找算法（顺序和折半）

# 简单选择排序
'''
def select_sort(items, comp=lambda x,y: x<y): # lambda x, y: x < y，也就是判断 x 是否小于 y，是则返回true

    # items = items[:] 
    # 虽然变量名都是 items，但实际上这行代码的作用是创建了一个新的列表对象，后续操作的 items 是新生成的列表，而并非原本的列表
    # 1、创建原始列表的一个浅拷贝，避免修改原始列表，
    # 2、代码可读性和一致性：使用相同的变量名可以让代码更具可读性，因为在函数内部，开发者可以像操作原始列表一样操作新生成的列表
    items = items[:] 
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index = j
        items[i],items[min_index] =  items[min_index], items[i]
    return items

# 测试代码
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = select_sort(test_list)
print(sorted_list)
print(test_list)
'''

 
# 冒泡排序
'''
def bubble_sort(items, comp=lambda x,y: x>y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items)-1-i):
            if comp(items[j],items[j+1]):
                items[j], items[j+1] = items[j+1],items[j]
                swapped=True
        if not swapped:
            break
    return items

test_list = [3, 1, 4, 1, 5, 9]
sorted_list = bubble_sort(test_list)
print(sorted_list)
print(test_list)
'''


# 搅拌排序(冒泡排序升级版) （鸡尾酒排序，Cocktail Shaker Sort）
# ​工作原理：是冒泡排序的一种变体，它在每一轮中进行双向遍历。首先从左到右进行冒泡，将最大的元素移动到末端；
# 然后从右到左进行冒泡，将最小的元素移动到起始端。这样可以在某些情况下减少总的遍历次数。
# ​时间复杂度：最坏情况下仍然是 O(n²)，但在某些数据集上表现优于普通冒泡排序。
# ​特点：双向遍历，可以同时移动最大和最小元素，减少了部分不必要的比较
'''
def bubble_sort2(items, comp=lambda x,y: x>y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j],items[j+1]):
                items[j],items[j+1] = items[j+1],items[j]
                swapped = True

        if swapped:
            swapped = False
            for j in range(len(items)-2-i,i,-1):
                if comp(items[j - 1], items[j]):
                    items[j],items[j-1] = items[j-1],items[j]
        if not swapped:
            break
    return items
       
test_list = [3, 1, 4, 1, 5, 9]
sorted_list = bubble_sort2(test_list)
print(sorted_list)
print(test_list)
'''



# 归并排序算法，归并排序是一种分治算法，其核心思想是将一个大问题分解为多个小问题，
# 分别解决这些小问题，然后将小问题的解合并起来得到原问题的解。
'''
def merge(items1, items2, comp=lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(list(items), comp)


def _merge_sort(items, comp):
    """归并排序"""
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)

# endregion
'''


#顺序查找
'''
def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1

list1=['harrypotter','rng','faker','liuyifei','sese']
test = seq_search(list1,'rng')
print(test)
'''


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1