# -*- coding: utf8 -*-
import requests, os
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
from selenium import webdriver

username = os.environ.get('username_moke08')
password = os.environ.get('password_moke08')


def login(*args):
    chrome_options = webdriver.ChromeOptions()
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 启动浏览器，获取网页源代码
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get("https://www.moke08.com/member.php?mod=logging&action=login")
    browser.find_element(By.NAME, "username").send_keys(username)
    browser.find_element(By.NAME, "password").send_keys(password)
    browser.find_element(By.NAME, "loginsubmit").click()
    browser.implicitly_wait(30)
    browser.find_element(By.CSS_SELECTOR, "a:nth-child(11) > font").click()
    browser.find_element(By.CSS_SELECTOR, "#kx img").click()
    browser.find_element(By.CSS_SELECTOR, "label:nth-child(3)").click()
    browser.find_element(By.CSS_SELECTOR, ".pn > strong").click()
    browser.get("https://www.moke08.com/plugin.php?id=k_misign:sign")
    browser.find_element(By.ID, "JD_sign").click()
    browser.quit()


if __name__ == "__main__":
    if username:
        login()
