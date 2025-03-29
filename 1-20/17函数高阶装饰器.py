'''
#基础形态
import random
import time

def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random()*6)
    print(f'{filename}下载完成.')

def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random()*6)
    print(f'{filename}上传完成.')

start = time.time()
download('Python从入门到放弃.pdf')
end = time.time()
print(f'下载用时：{end-start:.2f}秒')

start = time.time()
upload('Python从入门到放弃.pdf')
end = time.time()
print(f'上传用时：{end-start:.2f}秒')

'''



#装饰器形态

# 假设调用download('test.avi')，实际执行流程是：
# 1.调用wrapper('test.avi')
# 2.wrapper记录开始时间
# 3.wrapper调用原始download('test.avi')
# 4.原始download执行其代码
# 5.控制权返回给wrapper
# 6.wrapper记录结束时间并计算耗时
# 7.wrapper打印耗时信息
# 8.wrapper返回原始download的结果(如果有)
# 这种装饰器模式在不修改原始函数代码的情况下，为其添加了计时功能，体现了Python的装饰器强大之处。

import time
import random

def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random()*6)
    print(f'{filename}下载完成.')

def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random()*6)
    print(f'{filename}上传完成.')

def record_time(func):

    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        # 返回被装饰函数的返回值
        return result
    
    return wrapper

# 将 download = record_time(download) 这行代码理解为：
# 用 record_time 装饰 download，并把装饰后的结果重新赋值给 download。
# 也就是说，download 现在变成了一个新的函数，它已经被增强，拥有了计时功能。
download = record_time(download)
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

# 这样也可以，保留了原始的download函数，仍然可以直接调用download('...')（不带计时功能）
# 可以同时拥有计时版本(dold)和原始版本(download)，这在调试时特别有用
# 更直观地展示了装饰器就是"函数转换"的本质，record_time(download)返回一个新函数，你可以赋予它任何名字

#dold = record_time(download)  # 装饰器应用
#dold('MySQL从删库到跑路.avi')  # 调用



'''
#语法糖形态
import random
import time

def record_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result

    return wrapper


@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
'''



'''
def get_multiple_func(n):
    def multiple(x):
        return n * x    
    return multiple

double = get_multiple_func(2)
triple = get_multiple_func(3)

print(double(7))    # 14
print(triple(5))    # 15
'''