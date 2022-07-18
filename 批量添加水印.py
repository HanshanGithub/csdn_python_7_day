from os import sys, path, listdir
import os
from PIL import Image, ImageDraw, ImageFont
import shutil

fileList = []

def search(root, target):

    items = listdir(root)
    # print(items)
    for item in items:
        filepath = path.join(root, item)
        if path.isdir(filepath):
            search(filepath,target)
        elif path.isfile(filepath):
            if filepath.split('.')[-1] == target:
                fileList.append(filepath)
                print('[+]',filepath)
    return fileList

def moveFileToDestAddLogo(files,dest):
    for file in files:
        shutil.copy(file,dest)
        # shutil.copy2(file,dest)
    
    # 为dest目录中的文件添加水印
    names = os.listdir(dest)
    # 设置图片水印的字体的字号; 在外循环减少运行次数
    fontOne = ImageFont.truetype("C:/Windows/Fonts/STXINGKA.ttf", 76)
    fontTwo = ImageFont.truetype("C:/Windows/Fonts/STXINGKA.ttf", 76)
    for name in names:
        filename = dest + "\\" + name
        img = Image.open(filename)
        draw = ImageDraw.Draw(img)
         # 设置水印文字的位置（x,y)，文本，颜色，字体字号
        draw.text((img.size[0] / 4, img.size[1] / 4), "nit", fill=(255, 0, 0), font=fontOne)
        draw.text((img.size[0] / 4, img.size[1] / 4 + 80), "批量添加水印", fill=(20, 150, 200), font=fontTwo)
        img.save(filename)

def main(argv):
    path = argv[1]
    target = argv[2]
    dest = argv[3]
    files = search(path,target)
    moveFileToDestAddLogo(files,dest)
    # print(files)

if __name__ == '__main__':
    main(sys.argv)


