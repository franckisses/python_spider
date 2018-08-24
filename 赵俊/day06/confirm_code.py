"""
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 20:36
# @Author  : franck
# @Email   : franck_gxu@outlook.com
"""
# 导入pytesseract库
import pytesseract
# 导入Image库
from PIL import Image

# 指定tesseract.exe所在的路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# 打开图片
image = Image.open("1.JPG")
# 调用image_to_string将图片转换为文字
text = pytesseract.image_to_string(image)
print(text)