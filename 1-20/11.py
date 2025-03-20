'''
s = 'hello,world'
print(s.center(20, '*'))  # ****hello,world*****
print(s.ljust(20, '~'))   # hello,world********
print(s.rjust(20, '#'))   # ########hello,world
print(s.zfill(20))        # 000000000hello,world

'''

a=321
b=123
print('{0}*{1}={2}'.format(a,b,a*b))

s1='    jackfrued@126.com'
print(s1.strip())
s2='~你好，世界~'
print(s2.strip('~'))
print(s2.lstrip())
