'''
class Student:
    def __init__(self,name,age):
        self.__name = name
        self.age = age

    def study(self,course_name):
        print(f'{self.__name}正在学习{course_name}.')

stu = Student('孙悟空',20)
stu.study('Python程序设计')
print(stu.age)
print(stu.__name)
'''

'''
#动态语言：在运行时可以改变其结构的语言，例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化
#动态属性：在 Python 中，我们可以动态为对象添加属性，这是 Python 作为动态类型语言的一项特权
class Student:
    def __init__(self,name,age):
        self.name =name
        self.age=age

stu = Student('tom',20)
stu.sex = 'boy'

# 获取对象的属性字典
attributes = vars(stu)

# 逐个输出属性值
for value in attributes.values():
    print(value)
'''

'''
#如果不希望在使用对象时动态的为对象添加属性，可以使用 Python 语言中的__slots__魔法
class Student:
    __slots__ =('name','age')

    def __init__(self,name,age):
        self.name = name
        self.age = age

stu = Student('sunwukong',20)
stu.sex = 'boy'
'''

class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name}正在吃饭.')
    
    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生"""
    
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title
    
    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')



stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
tea1 = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')