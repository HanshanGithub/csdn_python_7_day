# 从PIL模块中导入Image对象，我们需要的缩放功能由Image对象提供
from PIL import Image
 
# 打开一个jpg图像，使用相对路径，打开文件的操作已经被Image对象库封装
img = Image.open('D:/cvpic/pic1.jpg')
 
# 获得图像尺寸:
w, h = img.size
 
# print打印字符串使用字符串格式化输出图像大小，字符串中的%s为占位符
print('源图像大小为: %sx%s' % (w, h))
# 宽，高各自除以2，缩小到原来的一半
img.thumbnail((w/2, h/2))
 
# 把缩放后的图像用jpeg格式保存:
img.save('D:/amstorage/thumbdog.jpg', 'jpeg')
 
