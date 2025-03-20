# xinhua = {
#     '麓': '山脚下',
#     '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
#     '蕗': '甘草的别名',
#     '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
# }

# print(xinhua)

# person ={
#     'first_name': '张',
#     'last_name': '三',
#     'age': 18,
#     'city': '北京'
# }
# print(person)
# print(len(person)) 
# for key in person:
#     print(key)
#     print(person[key])
# print('--------------------')
# for key, value in person.items():
#     print(key)
#     print(value)

#=========================================
#=========================================
# sentence = input('请输入一句话：')
# counter = {}
# for ch in sentence:
#     if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
#         counter[ch] = counter.get(ch, 0) + 1

# sorted_keys = sorted(counter,key=counter.get,reverse=True)

# for key in sorted_keys:
#     print(f'{key}出现了{counter[key]}次')


#=========================================
#=========================================

stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)
'''
阅读顺序：可以按照以下顺序来理解这行代码：
1.for key, value in stocks.items()：这部分是迭代部分，stocks.items() 方法会返回一个包含字典所有键值对的可迭代对象，
    每次迭代会将一个键值对分别赋值给变量 key 和 value。例如，第一次迭代时，key 可能是 'AAPL'，value 可能是 191.88。
2.if value > 100：这是筛选条件部分，只有当 value 大于 100 时，才会将当前的键值对包含在新字典中。
    如果 value 不满足这个条件，就会跳过当前键值对，继续下一次迭代。
3.key: value：这是生成新字典键值对的表达式部分，当某个键值对满足筛选条件时，就会将这个键值对添加到新字典中。
'''