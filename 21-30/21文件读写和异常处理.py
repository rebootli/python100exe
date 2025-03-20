'''
#读写文本文件
file = open(r'd:\VSCODE\python100exe\21-30\致橡树.txt', 'r', encoding='utf-8')
print(file.read())
file.close()
'''

file = open('致橡树.txt', 'r', encoding='utf-8')
print(file.read())
file.close()