
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


from lxml import etree
html = etree.parse('./页面解析和数据存储/test.html',etree.HTMLParser())
result = html.xpath('//*')
result2 = html.xpath('//li')
result3 = html.xpath('//li/a')
print(result3)
#print(result)
#print(result2)




