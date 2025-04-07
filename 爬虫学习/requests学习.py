'''
import requests

r = requests.get('https://www.baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text[:100])
print(r.cookies)

'''

'''
import requests

r = requests.get('https://httpbin.org/get')
print(r.json())
r = requests.post('https://httpbin.org/post')
r = requests.put('https://httpbin.org/put')
r = requests.delete('https://httpbin.org/delete')
r = requests.patch('https://httpbin.org/patch')

'''





'''
import requests

r = requests.get('https://httpbin.org/get')
print(r.text)
'''
#执行后如下
'''
{
  {
  "args": {},
  "headers ": {
    "Accept": "*/*",                    #表示客户端可以接收任何类型的响应内容。
    "Accept-Encoding": "gzip, deflate", #表示客户端支持 gzip 和 deflate 压缩格式（服务器可能会压缩响应以节省带宽）。
    "Host": "httpbin.org",              #请求的目标域名。
    "User-Agent": "python-requests/2.32.3",  #客户端的标识（这里是 Python 的 requests 库及其版本）。
    "X-Amzn-Trace-Id": "Root=1-67f07eb0-53f23dc42690bdad514e8e38"  #AWS 相关的追踪 ID（因为 httpbin.org 托管在 AWS 上）
  },
  "origin": "104.28.152.184",
  "url": "https://httpbin.org/get"
}
总结
字段	含义	            示例
args	URL 查询参数	   {"key": "value"}
headers	请求头	           包含客户端信息、支持的编码等
origin	客户端 IP 地址	   "123.45.67.89"
url	    请求的完整 URL	   "https://httpbin.org/get"
'''

#添加参数
'''
import requests

data = {
    'name':'germey',
    'age' :'25'
}

r = requests.get('https://httpbin.org/get',params=data)
print(r.text)
'''

'''
import requests

r = requests.get('https://httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))
'''


#抓取网页
'''
import requests
import re   # 正则表达式库，用于提取数据

r = requests.get('https://ssr1.scrape.center/')
pattern = re.compile('<h2.*?>(.*?)</h2>',re.S)
titles = re.findall(pattern,r.text)   #re.findall() 返回所有匹配正则的 子串列表。
print(titles)
'''

#抓取二进制数据，图片，视频，音频；然后保存本地
'''
import requests
r = requests.get('https://scrape.center/favicon.ico')

 # r.content 获取原始字节
 #'wb' 表示以 二进制写入模式 打开文件（w=写入，b=二进制）。
 # with 语句确保文件操作完成后自动关闭，避免资源泄露。
with open('favicon.ico','wb') as f:
    f.write(r.content)    #f.write() 将这些字节直接写入文件，生成与网络一致的 .ico 文件。
'''

'''
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://ssr1.scrape.center/', headers=headers)
print(r.text)
'''

'''
import requests

data = {'name':'germey', 'age':'25'}
r = requests.post("https://httpbin.org/post",data=data)
print(r.text)
'''

'''
import requests

r = requests.get('https://ssr1.scrape.center/')
print(type(r.status_code),r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history),r.history)
'''

# requests.codes码
'''
import requests

r = requests.get('https://ssr1.scrape.center/')
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
'''


#文件上传
'''
import requests

files = {'file': open('favicon.ico','rb')}
r = requests.post('https://httpbin.org/post',files=files)
print(r.text)
'''

#Cookie 设置

'''
import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)

for key,value in r.cookies.items():
    print(key + '=' + value)

headers = {
    'cookie':'_octo=GH1.1.1475985565.1741506734; GHCC=Required:1-Analytics:1-SocialMedia:1-Advertising:1; MicrosoftApplicationsTelemetryDeviceId=9400909b-6e30-4d27-b138-25e9a383e1e1; _device_id=783d3f2ec223690456175ed3fafa487b; MSFPC=GUID=faddf7c70fdc4f2c97f47c9c0fd0bed0&HASH=fadd&LV=202503&V=4&LU=1741479446502; saved_user_sessions=122135285%3ABJozYQ7UqVvApS-mHXy_Iz1bNrR2hthrYdNaPywNotL2VSr2; user_session=BJozYQ7UqVvApS-mHXy_Iz1bNrR2hthrYdNaPywNotL2VSr2; __Host-user_session_same_site=BJozYQ7UqVvApS-mHXy_Iz1bNrR2hthrYdNaPywNotL2VSr2; logged_in=yes; dotcom_user=rebootli; fileTreeExpanded=true; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; cpu_bucket=lg; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=UW6pZe8BpWZPDGFyNZkSqqTS1mVt5m9fxBZXRIu0pgue0HaYj0tq0xN4MvcFOvGFB9lgF5v4TQbKRJcRnY55MlmVeMRwmh5xfDLWSlKsROtIv9sTCkISQa3Y2LG3sTlRYsP6CgDGS4Sl2I4uxSxTd8AU1kjeBOBm6tWsp79JyxAxRLyGvrHdvaW3tjUfXo%2FwkFG9yfIRSNgJ6jMsMhhT%2BGmaOZkaZdyipT9t4K1pv%2FOcYz0s22ksrMqkNunDi1JmkrBef%2Bt7EIRRh8Nfznr2Fv2mcs2O2I5xhSGcTLst07UbM7TCmBys6ez5F1uqkLSORkTy1kN%2FPTjUzi7fITBl26Ljiupt9AbqHBWmOHwsy2xRsw9JkwyNLBcHGlt1%2B1Pj--oYDaKyJPcmbdN6D%2B--BxzTqRYwj6pRoK4eU8EwNg%3D%3D',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}

r = requests.get('http://github.com/',headers=headers)
print(r.text)
'''

#Session 维持
'''
import requests

#这个URL是 httpbin 提供的测试接口，服务端会返回一个 Set-Cookie 响应头，尝试设置 Cookie
requests.get('https://httpbin.org/cookies/set/number/123456789')
#这个接口会返回客户端（你的代码）当前携带的所有 Cookies
r = requests.get('https://httpbin.org/cookies')

print(r.text)  #实际输出结果为空，因为每个 requests.get() 请求都是独立的，默认不会自动保存或携带前一个请求的 Cookies

'''

'''   存入seession中
import requests

s = requests.Session()
s.get('https://httpbin.org/cookies/set/number/123456789')

r = s.get('https://httpbin.org/cookies')
print(r.text)
'''

# SSL 证书验证

'''
import requests

response = requests.get('https://ssr2.scrape.center/')
print(response.status_code)
'''

'''
import requests
from requests.packages import urllib3

urllib3.disable_warnings()
response = requests.get('https://ssr2.scrape.center/',verify=False)
print(response.status_code)
'''

'''
import logging
import requests

logging.captureWarnings(True)
response = requests.get('https://ssr2.scrape.center/',verify=False)
print(response.status_code)

'''


# 身份认证
# requests 自带的身份认证功能，
# 通过 auth 参数即可设置
'''
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('https://ssr3.scrape.center/',auth=HTTPBasicAuth('admin','admin'))
print(r.status_code)
'''

# 可以简写
'''
import requests

r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
print(r.status_code)
'''


# OAuth 认证，不过此时需要安装 oauth 包
# pip3 install requests_oauthlib

'''
import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)
'''




