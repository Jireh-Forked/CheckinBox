# -*- coding: utf8 -*-
import os

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver

SCKEY = os.environ.get('SCKEY')
cookie = os.environ.get('cookie_52programer')


def main(*args):
    msg = ""
    try:
        s = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
            'Cookie': cookie,
            'ContentType': 'text/html;charset=gbk',
            'DNT': '1'
        }
        url = "https://www.52programer.com/plugin.php?id=k_misign:sign"
        get_form_hash = s.get(url=url, headers=headers)
        b = BeautifulSoup(get_form_hash.text, 'html.parser')
        form_hash = b.find('input', {"name": "formhash"})["value"]
        sign_url = "https://www.52programer.com/plugin.php?id=k_misign:sign&operation=qiandao&formhash=" + form_hash + "&from=insign&inajax=1&ajaxtarget=JD_sign"
        get_sign = s.get(url=sign_url, headers=headers)
        bs = BeautifulSoup(get_sign.text, 'html.parser')
        if bs.text in "成功":
            if SCKEY:
                scurl = f"https://sc.ftqq.com/{SCKEY}.send"
                data = {
                    "text": "吾爱程序员签到成功",
                    "desp": "吾爱程序员签到成功"
                }
                requests.post(scurl, data=data)
            msg += "吾爱程序员签到成功！,"
            print("吾爱程序员签到成功")
        elif bs.text in "\n今日已签":
            msg += "吾爱程序员重复签到！,"
            print("吾爱程序员重复签到")
        else:
            print(bs.text)
    except Exception as e:
        print('repr(e):', repr(e))
        msg += '运行出错,repr(e):' + repr(e)
    return msg + "\n"


if __name__ == "__main__":
    if cookie:
        main()
