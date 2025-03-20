'''
import json

#将数据结构或对象状态转换为可以存储或传输的形式,序列化（serialization）
my_dict = {
    'name':'哈利波特',
    'age' : '18',
    'friends':['罗恩','赫敏'],
    'cars' :[
        {'brand':'xiaomi','max_speed':350},
        {'brand':'BMW','max_speed':240},
        {'brand':'Benz','max_speed':280}
    ]
}
print(json.dumps(my_dict))

with open('data.json','w') as file:
    json.dump(my_dict,file)

'''
'''
import json

#从一系列字节中提取数据结构的操作，就是反序列化
with open('data.json','r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)
'''


import requests

resp = requests.get('https://apis.tianapi.com/aqi/index?key=bfbf33a58ed81425fc5261ffbf70524e&area=上海')
if resp.status_code == 200:
    data_model = resp.json()
    print(data_model)
    print('-'*60)

    print(data_model['msg'])
    print(data_model['result'])
    print('-'*60)

    print(data_model['result']['area_code'])
    print(data_model['result']['pm2_5'])
    print('-'*60)