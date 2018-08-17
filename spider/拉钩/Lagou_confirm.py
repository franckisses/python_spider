"""
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 20:45
# @Author  : franck
# @Email   : franck_gxu@outlook.com
"""

import pytesseract,time
from urllib import request
from PIL import Image

def main():
    # 指定tesseract.exe所在的路径
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    url = "https://passport.lagou.com/vcode/create?from=login&refresh=1534423628430"
    while True:
        request.urlretrieve(url,"confirm.png")
        image = Image.open("confirm.png")
        text=pytesseract.image_to_string(image)
        print(text)
        time.sleep(5)

if __name__ =="__main__":
    main()
