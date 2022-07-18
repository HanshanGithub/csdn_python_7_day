"""
# 导入包
from PIL import Image, ImageDraw, ImageFont

# 图片路径，必须是当前目录下
file = "beach.jpg"
# 打开图片
img = Image.open(file)  
# 获取图片尺寸
print(img.size)
# 设置图片水印的字体的字号
fontOne = ImageFont.truetype("‪C:/Windows/Fonts/STXINGKA.ttf", 36)
fontTwo = ImageFont.truetype("‪C:/Windows/Fonts/STXINGKA.ttf", 36)

# 创建Draw对象，用于之后绘制文字
draw = ImageDraw.Draw(img)
# 设置水印文字的位置（x,y)，文本，颜色，字体字号
draw.text((img.size[0] / 11, img.size[1] / 20), "nit的水印添加测试", fill=(255, 0, 0), font=fontOne)
draw.text((img.size[0] / 11, img.size[1] / 20 + 40), "123abc!@#中国", fill=(20, 150, 200), font=fontTwo)
# 图片预览
img.show()
# 图片保存
img.save("DogWaterMark.jpg")
"""


# 导入包
from PIL import Image, ImageDraw, ImageFont

# 图片路径，可是当前目录下，也可是绝对路径
# file = "pic.bmp"
file = "D:\AmStorage\My_File\SCDN_test\jpg\缴费.jpg"
# 打开图片
img = Image.open(file)
# 获取图片尺寸
print(img.size)
# 设置图片水印的字体的字号
fontOne = ImageFont.truetype("C:/Windows/Fonts/STXINGKA.ttf", 76)
fontTwo = ImageFont.truetype("C:/Windows/Fonts/STXINGKA.ttf", 76)

# 创建Draw对象，用于之后绘制文字
draw = ImageDraw.Draw(img)
# 设置水印文字的位置（x,y)，文本，颜色，字体字号
draw.text((img.size[0] / 5, img.size[1] / 5), "nit的水印添加测试", fill=(255, 0, 0), font=fontOne)
draw.text((img.size[0] / 5, img.size[1] / 5 + 80), "123abc!@#中国", fill=(20, 150, 200), font=fontTwo)
# 图片预览
img.show()
# 图片保存
img.save("nvtuanWaterMark.jpg")

