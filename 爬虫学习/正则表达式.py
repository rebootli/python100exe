'''
group 方法可以输出匹配到的内容
span 方法可以输出匹配的范围
'''

'''
group(1)，它与 group() 有所不同，后者会输出完整的匹配结果，而前者会输出第一个被 () 包围的匹配结果。
假如正则表达式后面还有 () 包括的内容，那么可以依次用 group(2)、group(3) 等来获取
'''


'''
 .*   其中 . 可以匹配任意字符（除换行符），* 代表匹配前面的字符无限次，
 所以它们组合在一起就可以匹配任意字符了。
'''

# region 贪婪与非贪婪

'''
在贪婪匹配下，.* 会匹配尽可能多的字符。
正则表达式中 .* 后面是 \d+，也就是至少一个数字，并没有指定具体多少个数字，
因此，.* 就尽可能匹配多的字符，这里就把 123456 匹配了，
给 \d+ 留下一个可满足条件的数字 7，最后得到的内容就只有数字 7 了。
'''


'''
非贪婪匹配的写法是 .*?，多了一个 ?
贪婪匹配是尽可能匹配多的字符，非贪婪匹配就是尽可能匹配少的字符。
当 .*? 匹配到 Hello 后面的空白字符时，再往后的字符就是数字了，
而 \d+ 恰好可以匹配，那么这里 .*? 就不再进行匹配，交给 \d+ 去匹配后面的数字
'''


'''
做匹配的时候，字符串中间尽量使用非贪婪匹配，也就是用 .*? 来代替 .*，以免出现匹配结果缺失的情况。
但这里需要注意，如果匹配的结果在字符串结尾，.*? 就有可能匹配不到任何内容了，因为它会匹配尽可能少的字符
'''


# endregion

# region 修饰符re.S,匹配包括换行符在内的所有字符

# endregion

import re

html = '''
<div id="songs-list">
  <h2 class="title">经典老歌</h2>
  <p class="introduction">经典老歌列表</p>
  <ul id="list" class="list-group">
    <li data-view="2">一路上有你</li>
    <li data-view="7">
      <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
    </li>
    <li data-view="4" class="active">
      <a href="/3.mp3" singer="齐秦">往事随风</a>
    </li>
    <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
    <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
    <li data-view="5">
      <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
    </li>
  </ul>
</div>
'''

# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# if result:
#     print(result.group(1), result.group(2))


# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)
# print(type(results))

# for result in results:
#     print(result)
#     print(result[0], result[1], result[2])


# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
# for result in results:
#     print(result[1])


html = re.sub('<a.*?>|</a>', '', html)
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
for result in results:
    print(result.strip())








