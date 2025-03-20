'''
class Student:
    def study(self,course_name):
        print(f'学生正在学习{course_name}')
    
    def play(self):
        print(f'学生正在玩游戏')

stu1 = Student()
stu2 = Student()
print(stu1)    # <__main__.Student object at 0x10ad5ac50>
print(stu2)    # <__main__.Student object at 0x10ad5acd0> 
print(hex(id(stu1)), hex(id(stu2)))    # 0x10ad5ac50 0x10ad5acd0

# 通过“类.方法”调用方法
# 第一个参数是接收消息的对象
# 第二个参数是学习的课程名称
Student.study(stu1, 'Python程序设计')    # 学生正在学习Python程序设计.
# 通过“对象.方法”调用方法
# 点前面的对象就是接收消息的对象
# 只需要传入第二个参数课程名称
stu1.study('Python程序设计')             # 学生正在学习Python程序设计.

Student.play(stu2)                      # 学生正在玩游戏.
stu2.play()                             # 学生正在玩游戏. 
'''

import time
#定义时钟类
class CLOCK:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute    
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    
#创建时钟对象
clock = CLOCK(23,59,58)
while True:
    #给时钟对象发消息读取时间
    print(clock.show())
    #休眠1秒钟
    time.sleep(1)
    #给时钟对象发消息使其走动
    clock.run()