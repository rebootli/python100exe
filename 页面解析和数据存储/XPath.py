
# from lxml import etree
# text = '''
# <div>
#     <ul>
#         <li class="item-0"><a href="link1.html">first item</a></li>
#         <li class="item-1"><a href="link2.html">second item</a></li>
#         <li class="item-inactive"><a href="link3.html">third item</a></li>
#         <li class="item-1"><a href="link4.html">fourth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a>
#     </ul>
# </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))


# from lxml import etree

# html = etree.parse('./页面解析和数据存储/test.html',etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8')) 


# from lxml import etree
# html = etree.parse('./页面解析和数据存储/test.html',etree.HTMLParser())
# result = html.xpath('//*')   # * 代表匹配所有节点
# result2 = html.xpath('//li')  # //获取所有 li 节点
# result3 = html.xpath('//li/a') # /a 即选择了所有 li 节点的所有直接子节点 a

# //ul//a获取 ul 节点下的所有子孙节点 a
# 如果这里用 //ul/a，就无法获取任何结果了。
# 因为 / 用于获取直接子节点，而在 ul 节点下没有直接的 a 子节点，
# 只有 li 节点，所以无法获取任何匹配结果
#result4 = html.xpath('//ul//a') 
#print(result3)
#print(result)
#print(result2)



from lxml import etree

html = etree.parse('./页面解析和数据存储/test.html', etree.HTMLParser())

#result = html.xpath('//a[@href="link4.html"]/../@class')
#result = html.xpath('//a[contains(@href, "link")]/../@class')
#print(result)

# result  = html.xpath('//li[@class="item-0"]')
# print(result)

# result = html.xpath('//li[@class="item-0"]/a/text()')
# print(result)

# 属性获取
# result = html.xpath('//li/a/@href')
# print(result)


#属性多值匹配
# from lxml import etree
# text='''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[@class="li"]/a/text()')
# print(result)

# result = html.xpath('//li[contains(@class,"li")]/a/text()')
# print(result)


# ====================================
# 多属性匹配（重点）
# ====================================
# from lxml import etree
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''

# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
# print(result)



# region  按序选择，利用中括号传入索引的方法,获取特定次序的节点

# from lxml import etree

# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''

# html = etree.HTML(text)
# result = html.xpath('//li[1]/a/text()') #序号是以 1 开头的
# print(result)

# result = html.xpath('//li[last()]/a/text()')
# print(result)

# result = html.xpath('//li[position()<3]/a/text()')
# print(result)

# result = html.xpath('//li[last()-2]/a/text()')
# print(result)

# endregion 





