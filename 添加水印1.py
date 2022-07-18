# 导入包
from PIL import Image, ImageDraw, ImageFont

# 图片路径，必须是当前目录下
imagefile = "beach.jpg"
# 打开图片
imageInfo = Image.open(imagefile)
# 获取图片尺寸
print(imageInfo.size)
# 设置图片水印的字体的字号
fontOne = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 36)
fontTwo = ImageFont.truetype("C:/Windows/Fonts/STXINGKA.ttf", 36)

# 创建Draw对象，用于之后绘制文字
draw = ImageDraw.Draw(imageInfo)
# 设置水印文字的位置（x,y)，文本，颜色，字体字号
draw.text((imageInfo.size[0] / 11, imageInfo.size[1] / 20), "nit的水印添加测试", fill=(255, 0, 0), font=fontOne)
draw.text((imageInfo.size[0] / 11, imageInfo.size[1] / 20 + 40), "123abc!@#中国", fill=(20, 150, 200), font=fontTwo)
# 图片预览
imageInfo.show()
# 图片保存
imageInfo.save("nvtuanWaterMark.jpg")
