'''
#读写文本文件
file = open(r'd:\VSCODE\python100exe\21-30\致橡树.txt', 'r', encoding='utf-8')
print(file.read())
file.close()
'''
'''
#不是考虑此代码和文件是否在一起，而是考虑终端的位置是否和'致橡树.txt'在一起
#报错后，使用cd D:\VSCODE\python100exe\21-30  让终端进入21-30文件夹里。
file = open('致橡树.txt', 'r', encoding='utf-8')
print(file.read())
file.close()
'''

'''
#逐行读取
file = open('致橡树.txt','r',encoding='utf-8')
for line in file:
    print(line,end='')
file.close()

#按行读取到一个列表容器
file = open('致橡树.txt','r',encoding='utf-8')
lines = file.readlines()
for line in lines:
    print(line,end='')
file.close()
'''
'''
#向文件中写入内容，可以在打开文件时使用w,或者a作为操作模式
#前者会截断之前的文本内容写入新的内容
#后者是在原来内容的尾部追加新的内容。

file = open('致橡树.txt','a',encoding='utf-8')
file.write('\n标题：《致橡树》')
file.write('\n作者：舒畅')
file.write('\n时间：2014年6月')
file.close()

'''
'''
#Python中和异常相关的关键字try、except、else、finally和raise
#在except后面，我们还可以加上else代码块，这是try 中的代码没有出现异常时会执行的代码，而且else中的代码不会再进行异常捕获
file = None
try:
    file = open('致橡树.txt','r',encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件！')
except LookupError:
    print('指定了未知编码！')
except UnicodeDecodeError:
    print('读取文件时解码错误！')
finally:
    if file:
        file.close()
'''

#在Python中，可以使用raise关键字来引发异常（抛出异常对象），
# 而调用者可以通过try...except...结构来捕获并处理异常
'''
class InputError(ValueError):
    pass

def fac(num):
    if num<0:
        raise InputError('只能计算非负整数的阶乘')
    if num in (0,1):
        return 1
    return num * fac(num -1)

flag = True
while flag:
    num = int(input('n = '))
    try:
        print(f'{num} != {fac(num)}')
        flag = False
    except InputError as err:
        print(err)
'''


#将阶乘函数改为迭代方式，避免递归深度问题。
#添加对用户输入是否为有效整数的验证，防止因输入非整数而导致的错误。
'''
class InputError(ValueError):
    pass

def fac(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

while True:
    try:
        num = int(input('n = '))
        if num < 0:
            raise InputError('只能计算非负整数的阶乘')
        print(f'{num} != {fac(num)}')
        break
    except ValueError:
        print('输入无效，请输入一个整数。')
    except InputError as err:
        print(err)
'''

# 还可以使用with上下文管理器语法在文件操作完成后自动执行文件对象的close方法，
# 这样可以让代码变得更加简单优雅，因为不需要再写finally代码块来执行关闭文件释放资源的操作
# 并不是所有的对象都可以放在with上下文语法中，只有符合上下文管理器协议（有__enter__和__exit__魔术方法）的对象才能使用这种语法，
# 直接尝试使用 with 语句,若对象实现了上下文管理器协议，with 语句就能正常执行；若未实现，就会抛出 AttributeError 异常
# Python标准库中的contextlib模块也提供了对with上下文语法的支持
'''
try:
    with open('致橡树.txt','r',encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
'''


# 读写二进制文件
# 在使用open函数打开文件时，如果要进行读操作，操作模式是'rb'，如果要进行写操作，操作模式是'wb'
# 读写文本文件时，read方法的返回值以及write方法的参数是str对象（字符串），
# 而读写二进制文件时，read方法的返回值以及write方法的参数是bytes-like对象（字节串）
# 下面的代码实现了将当前路径下名为guido.jpg的图片文件复制到吉多.jpg文件中的操作
'''
try:
    with open('guido.jpg','rb') as file1:
        data = file1.read()
    with open('lyf.jpg','wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')
'''

# 如果要复制的图片文件很大，一次将文件内容直接读入内存中可能会造成非常大的内存开销，
# 为了减少对内存的占用，可以为read方法传入size参数来指定每次读取的字节数，
# 通过循环读取和写入的方式来完成上面的操作，代码如下所示。

try:
    with open('guido.jpg','rb') as file1,open('lyf.jpg','wb') as file2:
        data = file1.read(512)
        while data:
            file2.write(data)
            data = file1.read()
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')


#ai改进代码；使得每一次提取，都是512字节
try:
    with open('guido.jpg', 'rb') as file1, open('lyf.jpg', 'wb') as file2:
        data = file1.read(512)
        while data:
            file2.write(data)
            data = file1.read(512)
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')





#不要使用异常机制来处理正常业务逻辑或控制程序流程，简单的说就是不要滥用异常机制，这是初学者常犯的错误。





