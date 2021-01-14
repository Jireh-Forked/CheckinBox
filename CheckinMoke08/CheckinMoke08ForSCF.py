# -*- coding: utf8 -*-
import os
from selenium.webdriver.common.by import By
from selenium import webdriver

username = os.environ.get('username_moke08')
password = os.environ.get('password_moke08')


def login(*args):
    chrome_options = webdriver.ChromeOptions()
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver

    # 启动浏览器，获取网页源代码
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
    browser.get("https://www.moke08.com/member.php?mod=logging&action=login")
    browser.find_element(By.NAME, "username").send_keys(username)
    browser.find_element(By.NAME, "password").send_keys(password)
    browser.find_element(By.NAME, "loginsubmit").click()
    browser.implicitly_wait(60)
    try:
        browser.find_element(By.CSS_SELECTOR, "a:nth-child(11) > font").click()
        browser.find_element(By.CSS_SELECTOR, "#kx img").click()
        browser.find_element(By.CSS_SELECTOR, "label:nth-child(3)").click()
        browser.find_element(By.CSS_SELECTOR, ".pn > strong").click()
    except:
        print("无法找到签到按钮1，或已经签到")

    browser.get("https://www.moke08.com/plugin.php?id=k_misign:sign")

    try:
        browser.find_element(By.ID, "JD_sign").click()
    except:
        print("无法找到签到按钮2，或已经签到")

    browser.quit()


if __name__ == "__main__":
    if username:
        print("----------小云社区开始尝试签到----------")
        login()
        print("----------小云社区结束签到----------")
