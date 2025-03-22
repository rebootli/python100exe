
# pip install pillow

from PIL import Image

# 读取图像获得Image对象
image = Image.open('resources/guido.jpg')

# 通过Image对象的format属性获得图像的格式
print(image.format)

# 通过Image对象的size属性获得图像的尺寸
print(image.size)

# 通过Image对象的mode属性获取图像的模式
print(image.mode)

'''
# 通过Image对象的show方法显示图像
image.show()

# 通过Image对象的crop方法指定剪裁区域剪裁图像
image.crop((80, 20, 310, 360)).show()

# 通过Image对象的thumbnail方法生成指定尺寸的缩略图
image.thumbnail((128, 128))
image.show()
'''

#缩放和黏贴图像
'''
# 读取骆昊的照片获得Image对象
luohao_image = Image.open('resources/IMG_20180222_182102.jpg')
# 读取吉多的照片获得Image对象
guido_image = Image.open('resources/guido.jpg')

# 从吉多的照片上剪裁出吉多的头
guido_head = guido_image.crop((80, 20, 310, 360))
width, height = guido_head.size
# 使用Image对象的resize方法修改图像的尺寸
# 使用Image对象的paste方法将吉多的头粘贴到骆昊的照片上
luohao_image.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
luohao_image.show()
'''

#旋转和翻转
'''
image = Image.open('resources/guido.jpg')
# 使用Image对象的rotate方法实现图像的旋转
image.rotate(45).show()
# 使用Image对象的transpose方法实现图像翻转
# Image.FLIP_LEFT_RIGHT - 水平翻转
# Image.FLIP_TOP_BOTTOM - 垂直翻转
image.transpose(Image.FLIP_TOP_BOTTOM).show()
'''

#操作像素
'''
for x in range(80, 310):
    for y in range(20, 360):
        # 通过Image对象的putpixel方法修改图像指定像素点
        image.putpixel((x, y), (148, 128, 128))
image.show()
'''