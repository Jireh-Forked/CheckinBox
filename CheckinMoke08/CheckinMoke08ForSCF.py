# -*- coding: utf8 -*-
import requests, os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

cookie = os.environ.get('cookie_moke08')

def pjCheckin(*args):
    try:
        SCKEY = os.environ.get('SCKEY')
        s = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4298.4 Safari/537.36',
            'Cookie': cookie,
            'ContentType': 'text/html;charset=gbk',
            'DNT': '1'
        }
        a = s.get('https://www.moke08.com/plugin.php?id=k_misign:sign&operation=qiandao&formhash=c9912ec0&format=empty',
                  headers=headers)
        b = BeautifulSoup(a.text, 'html.parser')
        c = b.find('div', id='info').find('p').text

        if "您当前的访问请求当中含有非法字符，已经被系统拒绝" in c:
            if SCKEY:
                scurl = f"https://sc.ftqq.com/{SCKEY}.send"
                data = {
                    "text": "52pojie  Cookie过期",
                    "desp": c
                }
                requests.post(scurl, data=data)
            print("cookie_52pj失效，需重新获取")
        elif "恭喜" in c:
            print("52pj签到成功")
        else:
            print(c)
    except:
        print(b)
        print("52pj出错")


def login(*args):
    chrome_options = webdriver.ChromeOptions()
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 启动浏览器，获取网页源代码
    browser = webdriver.Chrome(chrome_options=chrome_options)
    mainUrl = "https://www.taobao.com/"
    browser.get(mainUrl)
    print(f"browser text = {browser.page_source}")
    browser.quit()


if __name__ == "__main__":
    if cookie:
        pjCheckin()
