
# def calc(*args,**kwargs):
#     items = list(args) + list(kwargs.values())
#     result = 0
#     for item in items:
#         if type(item) in (int,float):
#             result += item
#     return result

def calc(init_value,op_func,*args,**kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int,float):
            result = op_func(result,item)
    return result

def add(x,y):
    return x+y

def mul(x,y):
    return x*y

print(calc(0,add,1,2,3,4,5))
print(calc(1,mul,1,2,3,4,5))

