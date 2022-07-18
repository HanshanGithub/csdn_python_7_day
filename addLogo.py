# 导入包
from PIL import Image, ImageDraw, ImageFont
from os import sys, path, listdir
import os

def addLogo(dest):
    names = os.listdir(dest)
    print(names)
    # 设置图片水印的字体的字号; 在外循环减少运行次数
    fontOne = ImageFont.truetype("C:/Windows/Fonts/STXINGKA.ttf", 76)
    fontTwo = ImageFont.truetype("C:/Windows/Fonts/STXINGKA.ttf", 76)
    for name in names:
        filename = dest + "\\" + name
        img = Image.open(filename)
        draw = ImageDraw.Draw(img)
         # 设置水印文字的位置（x,y)，文本，颜色，字体字号
        draw.text((img.size[0] / 4, img.size[1] / 4), "nit", fill=(255, 0, 0), font=fontOne)
        draw.text((img.size[0] / 4, img.size[1] / 4 + 280), "批量添加水印", fill=(20, 150, 200), font=fontTwo)
        img.save(name)

def main():
    addLogo("D:\AmStorage\My_File\Photo\MyPhoto")

main()
    
