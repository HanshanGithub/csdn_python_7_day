from PIL import Image, ImageFilter
 
# 打开一个jpg图像文件，注意是当前路径:
img = Image.open('D:/cvpic/puppy.bmp')
# 应用模糊滤镜:
img1 = img.filter(ImageFilter.BLUR)
img2 = img.filter(ImageFilter.CONTOUR)
img3 = img.filter(ImageFilter.DETAIL)
img4 = img.filter(ImageFilter.EDGE_ENHANCE)
img5 = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
img6 = img.filter(ImageFilter.EMBOSS)
img7 = img.filter(ImageFilter.FIND_EDGES)
img8 = img.filter(ImageFilter.SHARPEN)
img9 = img.filter(ImageFilter.SMOOTH)
#img10 = img.filter(ImageFilter.SMOOTH_MORE_)

img1.save('blurDog_BLUR.jpg', 'jpeg')
img2.save('blurDog_CONTOUR.jpg', 'jpeg')
img3.save('blurDog_DETAIL.jpg', 'jpeg')
img4.save('blurDog_EDGE_ENHANCE.jpg', 'jpeg')
img5.save('blurDog_EDGE_ENHANCE_MORE.jpg', 'jpeg')
img6.save('blurDog_EMBOSS.jpg', 'jpeg')
img7.save('blurDog_FIND_EDGES.jpg', 'jpeg')
img8.save('blurDog_SHARPEN.jpg', 'jpeg')
img9.save('blurDog_SMOOTH.jpg', 'jpeg')
#img10.save('blurDog10.jpg', 'jpeg')

img.close()
