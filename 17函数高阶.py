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


'''
#装饰器形态
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



download = record_time(download)
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
 '''



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