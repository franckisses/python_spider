"""
# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 15:36
# @Author  : franck
# @Email   : franck_gxu@outlook.com
"""

import requests,json
class Spider:
    def __init__(self):
        self.formdata = {
            'params':'jBLRwxQXvkCkQjPo9mHIZL/6ePG2DVW0MQIFoEJBNiMMRzHxJxHItVjuUbc5ynHcdxr+FefqMzlb4R7Z2apacXFD0MSXZyICSFo1IwS5azi6oQg7uzJFNGIckYEWZmDGmyQBfCvDCw1g+QErnns93kjWgqhMealy/GNrZvPSsDKHCIwl4uBmXA6ogKFLdtmw',
            'encSecKey': '5f0469282230805748494c318683ccb05bc637a5027bf766bb2615cadfa8d8683906f3004e8ad4cc3fd8c8243b4ec0aa8eb99865f2e3eeadbe15bfa92f9f56d699201a19aaef0fae547b40765139234dd1d3958ec32645f28cd85b9b6037eb41754bcefc2a8b056c209180e09f824b6b1e87af6332733d243b651affb0750890'
        }
        self.headers ={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        self.url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_31445772?csrf_token="

    def __get_htmls(self,url):
        htmls = requests.post(url,data=self.formdata,headers=self.headers)
        return htmls.text
    def run(self):
        a =self.__get_htmls(self.url)
        s = json.loads(a)["hotComments"]
        for x in s:
            print("*"*30)
            print("昵称:",x['user']['nickname'])
            print("点赞数:",x['likedCount'])
            print("评论:",x['content'])
def main():
    spider = Spider()
    spider.run()

if __name__ == "__main__":
    main()


