# -*- coding: utf8 -*-
import requests, os
import json
import random
import string

username = os.environ.get('username_houqijun')
password = os.environ.get('password_houqijun')


class randoms():
    # 获取26个大小写字母
    letters = string.ascii_letters
    # 获取26个小写字母
    Lowercase_letters = string.ascii_lowercase
    # 获取26个大写字母
    Capital = string.ascii_uppercase
    # 获取阿拉伯数字
    digits = string.digits


def pjCheckin(*args):
    try:
        SCKEY = os.environ.get('SCKEY')
        s = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
            'Cookie': 'PHPSESSID=' + code(),
            'ContentType': 'text/html;charset=gbk',
            'DNT': '1'
        }
        url = "http://www.houqijun.vip/Passport_runLogin.html"
        loginData = {
            "from": "http://www.houqijun.vip/",
            "username": username,
            "password": password,
        }

        login = s.post(url=url, data=loginData, headers=headers)
        a = s.get('http://www.houqijun.vip/Center_runQiandao.html',
                  headers=headers)
        data = json.loads(a.text)

        if data['code'] == '1':
            if SCKEY:
                scurl = f"https://sc.ftqq.com/{SCKEY}.send"
                data = {
                    "text": "后期菌签到成功",
                    "desp": "后期菌签到成功"
                }
                requests.post(scurl, data=data)
            print("后期菌签到成功")
        elif data['code'] == '0':
            print("重复签到")
        else:
            print(data)
    except:
        print(data)
        print("签到出错")


def code():
    # s是小写字母和数字的集合
    s = randoms.Lowercase_letters + randoms.digits
    # 生成28位小写和数字的集合，并将列表转字符串
    code = ''.join(random.sample(s, 28))
    return code


if __name__ == "__main__":
    if username:
        print("----------后期菌开始尝试执行日常任务----------")
        pjCheckin()
        print("----------后期菌完成日常任务签到----------")
