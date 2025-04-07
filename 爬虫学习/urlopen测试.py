#import urllib.request

# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))

# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Date'))


'''
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
response = urllib.request.urlopen('https://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))
'''


'''
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('https://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
'''

'''
import urllib.request

request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
'''

'''
from urllib import request, parse

url = 'https://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {'name': 'germey'}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
'''


'''
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'

p= HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
'''

'''
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy_hander = ProxyHandler(
    {
        'http':'http://127.0.0.1:8080',
        'https':'https://127.0.0.1:8080'
    }
)

openr = build_opener(proxy_hander)
try:
    response = openr.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
'''

'''
import http.cookiejar,urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')

for item in cookie:
    print(item.name + "=" + item.value)
    print()
'''
'''
import urllib.request,http.cookiejar

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')

cookie.save(ignore_discard=True,ignore_expires=True)

'''

'''
import urllib.request,http.cookiejar

filename = 'cookielwp.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')

cookie.save(ignore_discard=True,ignore_expires=True)

'''
# 文件总是生成在脚本所在目录
'''
import os
import urllib.request, http.cookiejar

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, 'cookielwp.txt')

cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')

cookie.save(ignore_discard=True,ignore_expires=True)
'''


'''
import urllib.request, http.cookiejar

cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookielwp.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))
'''

'''
from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result)

print('=======================')

from urllib.parse import urlparse

result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)
'''

from urllib.parse import urlencode

params = {
    'name':'germey',
    'age':25
}

base_url = 'https://www.baidu.com'
url = base_url + urlencode(params)
print(url)


